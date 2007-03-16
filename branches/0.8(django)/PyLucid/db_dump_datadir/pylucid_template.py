table = 'pylucid_template'
fields = ['id', 'name', 'lastupdateby', 'description', 'content', 'lastupdatetime', 'createtime']
records = [
[1, 'basic', 14, 'default template', '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<title>PyLucid CMS - <lucidTag:page_title/></title>\n<meta name="robots"                    content="<lucidTag:robots/>" />\n<meta name="keywords"                  content="<lucidTag:page_keywords/>" />\n<meta name="description"               content="<lucidTag:page_description/>" />\n<meta name="Author"                    content="PyLucidCMS" />\n<meta name="DC.Date"                   content="<lucidTag:page_last_modified/>" />\n<meta name="DC.Date.created"           content="<lucidTag:page_datetime/>" />\n<meta http-equiv="Content-Type"        content="text/html; charset=utf-8" />\n<meta name="MSSmartTagsPreventParsing" content="TRUE" />\n<meta http-equiv="imagetoolbar"        content="no" />\n<lucidTag:page_style/>\n</head>\n<body>\n<div id="headline">\n  <a href="/">PyLucid CMS</a>\n</div>\n\n<div id="the_menu">\n  <lucidTag:main_menu/>\n  <div id="searching">\n    <lucidTag:search/>\n  </div>\n  <a href="http://sourceforge.net/projects/pylucid/" id="logo" alt="goto our SourceForge project page &gt;&gt;" title="goto our SourceForge project page &gt;&gt;">\n    <img src="http://sourceforge.net/sflogo.php?group_id=146328&amp;type=1" width="88" height="31" border="0" alt="SourceForge Logo" />\n  </a>\n</div>\n\n<div id="main_content">\n  <h2 id="page_title"><lucidTag:page_title/></h2>\n  <lucidTag:page_msg/>\n  <lucidTag:admin_menu/>\n  <lucidTag:page_body/>\n</div>\n\n<p id="footer">\n   powered by <lucidTag:powered_by/> | <lucidTag:script_login/> | Rendered in <lucidTag:script_duration/> sec. | last modified: <lucidTag:page_last_modified/>\n</p>\n\n</div>\n</body>\n</html>', '2007-02-05 08:30:55', None]
[6, 'small_dark', 14, "clone of 'basic'", '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<title>PyLucid CMS - <lucidTag:page_title/></title>\n<meta name="robots"                    content="<lucidTag:robots/>" />\n<meta name="keywords"                  content="<lucidTag:page_keywords/>" />\n<meta name="description"               content="<lucidTag:page_description/>" />\n<meta name="Author"                    content="PyLucidCMS" />\n<meta name="DC.Date"                   content="<lucidTag:page_last_modified/>" />\n<meta name="DC.Date.created"           content="<lucidTag:page_datetime/>" />\n<meta http-equiv="Content-Type"        content="text/html; charset=utf-8" />\n<meta name="MSSmartTagsPreventParsing" content="TRUE" />\n<meta http-equiv="imagetoolbar"        content="no" />\n<lucidTag:page_style/>\n</head>\n<body>\n<div id="content">\n  <p id="head">PyLucid CMS</p>\n  <hr class="big" />\n  <lucidTag:main_menu/>\n  <hr class="small" />\n\n  <h1><lucidTag:page_title/></h1>\n\n  <lucidTag:page_msg/><lucidTag:admin_menu/>\n\n  <lucidTag:page_body/>\n\n  <hr class="small" />\n  <hr class="big" />\n  <p id="nav_footer">\n    <lucidTag:page_last_modified/> | <lucidTag:script_login/> | Rendered in <lucidTag:script_duration/> sec. | <lucidTag:powered_by/>\n  </p>\n</div>\n</body>\n</html>', '2007-01-09 14:43:33', '2007-01-09 14:38:14']
[7, 'elementary', 14, "clone of 'basic'", '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<title>PyLucid CMS - <lucidTag:page_title/></title>\n<meta name="robots"                    content="<lucidTag:robots/>" />\n<meta name="keywords"                  content="<lucidTag:page_keywords/>" />\n<meta name="description"               content="<lucidTag:page_description/>" />\n<meta name="Author"                    content="PyLucidCMS" />\n<meta name="DC.Date"                   content="<lucidTag:page_last_modified/>" />\n<meta name="DC.Date.created"           content="<lucidTag:page_datetime/>" />\n<meta http-equiv="Content-Type"        content="text/html; charset=utf-8" />\n<meta name="MSSmartTagsPreventParsing" content="TRUE" />\n<meta http-equiv="imagetoolbar"        content="no" />\n<lucidTag:page_style/>\n</head>\n<body>\n<div id="headline"><h2>PyLucid CMS</h2></div>\n\n<lucidTag:main_menu/>\n\n<div id="main_content">\n  <h2 id="page_title"><lucidTag:page_title/></h2>\n  <lucidTag:page_msg/><lucidTag:admin_menu/>\n  <p id="back_links"><lucidTag:back_links/></p>\n\n  <lucidTag:page_body/>\n</div>\n\n<p id="footer">\n   powered by <lucidTag:powered_by/> | <lucidTag:script_login/> | Rendered in <lucidTag:script_duration/> sec. | last modified: <lucidTag:page_last_modified/>\n</p>\n\n</div>\n</body>\n</html>', '2007-01-09 15:49:32', '2007-01-09 15:13:53']
[8, 'small_white', 14, "clone of 'elementary'", '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">\n<head>\n<meta http-equiv="content-type" content="text/html; charset=utf-8" />\n<meta name="author" content="Martin Bergner/ Jens Diemer / Original design: Andreas Viklund - http://andreasviklund.com" />\n<meta name="robots" content="<lucidTag:robots/>" />\n<meta name="keywords" content="<lucidTag:page_keywords/>" />\n<meta name="description" content="<lucidTag:page_description/>" />\n<meta name="DC.Date" content="<lucidTag:page_last_modified/>" />\n<meta name="DC.Date.created" content="<lucidTag:page_datetime/>" />\n<meta name="MSSmartTagsPreventParsing" content="TRUE" />\n<meta http-equiv="imagetoolbar" content="no" />\n<lucidTag:page_style/>\n<!-- RSS: Insert your rss plugins here -->\n<!-- RSS: end -->\n<title>PyLucid - <lucidTag:page_title/></title>\n</head>\n<body>\n<div id="wrap">\n  <!-- HEADER: Put whatever you want in your header here -->\n  <div id="header">\n    This could be <strong>your</strong> header!\n  </div>\n  <!-- HEADER: end-->\n\n  <!-- Put your logo here -->\n  <!--\n     <img id="frontphoto" src="/img/logo.png" width="760" height="113" alt="" />\n  -->\n\n  <!-- LEFTSIDE: Here can be your menu, news and other things -->\n  <div id="leftside">\n    <h2 class="hide">Menu:</h2>\n    <lucidTag:main_menu/>\n    <lucidTag:search/>\n    </div>\n  <!-- LEFTSIDE: end -->\n  <!-- CONTENT: Here is the main page -->\n  <div id="contentwide">\n    <div id="admin"><lucidTag:admin_menu/></div>\n    <lucidTag:page_msg/>\n    <p id="nav_link">\n      <lucidTag:back_links/>\n\n    </p>\n    <lucidTag:page_body/>\n  </div>\n  <!-- CONTENT: end -->\n  <!-- FOOTER: Put your footer here -->\n  <div id="footer">\n    <p>\n      <lucidTag:script_login/> | Powered by <lucidTag:powered_by/>.\n    </p>\n\n  </div>\n  <!-- FOOTER: end -->\n</div>\n</body>\n</html>', '2007-01-15 12:02:46', '2007-01-15 11:36:14']
[9, 'old_basic', 14, "clone of 'basic'", '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<title>PyLucid CMS - <lucidTag:page_title/></title>\n<meta name="robots"                    content="<lucidTag:robots/>" />\n<meta name="keywords"                  content="<lucidTag:page_keywords/>" />\n<meta name="description"               content="<lucidTag:page_description/>" />\n<meta name="Author"                    content="PyLucidCMS" />\n<meta name="DC.Date"                   content="<lucidTag:page_last_modified/>" />\n<meta name="DC.Date.created"           content="<lucidTag:page_datetime/>" />\n<meta http-equiv="Content-Type"        content="text/html; charset=utf-8" />\n<meta name="MSSmartTagsPreventParsing" content="TRUE" />\n<meta http-equiv="imagetoolbar"        content="no" />\n<lucidTag:page_style/>\n</head>\n<body>\n<div id="headline"><h2>PyLucid CMS</h2></div>\n<div id="sidebar">\n<lucidTag:main_menu/>\n</div>\n\n<div id="main-content">\n  <h2><lucidTag:page_title/></h2>\n  <lucidTag:page_msg/><lucidTag:admin_menu/>\n  <p id="nav_link">\n    <lucidTag:back_links/>\n  </p>\n  <lucidTag:page_body/>\n  <p id="nav_footer">\n    <lucidTag:page_last_modified/> | <lucidTag:script_login/> | Rendered in <lucidTag:script_duration/> sec. | <lucidTag:powered_by/>\n  </p>\n</div>\n</body>\n</html>', '2007-02-05 08:29:21', '2007-02-05 08:29:21']
]
