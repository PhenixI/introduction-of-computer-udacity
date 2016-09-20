page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
begin_link = page.find('"',start_link);
end_link = page.find('"',begin_link+1)
url = page[begin_link+1:end_link] 
