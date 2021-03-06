# -*- coding: utf-8 -*-

"""
convert audio files with eac3to to AC3

DRAG&DROP audio file(s)
"""

import os, sys
import subprocess

from shared.config import VideoToolsConfig

from shared.tk_tools import askopenfilename2, simple_input
from shared.tools import subprocess2


PARAM_KEY = "lastac3"


def get_out_filename(fn, parameters):
    """
    build the out filename by striping some parts of the filename out.
    IMPORTANT:
        dependent on the filename builded in: eac3to.VideoFile.get_command()
    """
    def startendswith(txt, method, item_list):
        assert method in ("endswith", "startswith")
        
        ubound_method = getattr(txt, method)
        for item in item_list:
            if ubound_method(item):
                return True
        return False
            
    base_fn = os.path.splitext(fn)[0]
    
    parts1 = []    
    for part1 in base_fn.rsplit(" - "):
        part1 = part1.strip()
        parts = []
        for part in part1.split(","):
            part = part.strip()
            if part:
                if startendswith(part, "endswith", ("bits", "kbps", "khz")):
                    continue
                if startendswith(part, "startswith", ("DTS", "TrueHD")): 
                    continue
            parts.append(part)
        parts1.append(", ".join(parts))
    
    parts1 += [p.strip(" -") for p in parameters]
    basename = " - ".join(parts1) 
    return basename + ".ac3"    


if __name__ == "__main__":
    cfg = VideoToolsConfig()
    cfg.debug()
    
    files = sys.argv[1:]
    if not files:     
        files = askopenfilename2(
            title = "Choose the source file(s):",
            initialdir = cfg["last sourcedir"],
            multiple = True
#            filetypes = [('M2TS File','*.*')],
        )
    assert isinstance(files, list)   


    if PARAM_KEY not in cfg:
        cfg[PARAM_KEY] = ["-384, -down6"]
        
    new_values = simple_input(      
        title="eac3to parameters",
        pre_lable="Please input the used parameters (separated by comma!):",
        init_value=cfg[PARAM_KEY][0],
        post_lable="last values: %r\nUse nothing for only demuxing!" % cfg[PARAM_KEY],
    )
    parameters = [i.strip() for i in new_values.split(",")]
    parameters = [i for i in parameters if i] # delete emty items
    
    for fn in files:
        print fn
        out_fn = get_out_filename(fn, parameters)
        print out_fn
        
        cmd = [cfg["eac3to"], fn, out_fn] + parameters
        print "run '%s'..." % " ".join(cmd)
        process = subprocess.Popen(cmd, shell=True)
        process.wait()
        print
        
    # Store new parameters into cfg
    new_values = ", ".join(parameters)
    if new_values not in cfg[PARAM_KEY]:
        cfg[PARAM_KEY].insert(0, new_values)
        cfg[PARAM_KEY] = cfg[PARAM_KEY][:cfg["max save"]] # Cut to mutch values
        cfg.save_config()