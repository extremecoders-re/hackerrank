var start = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html";

function getDocumentXml(url)
{
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() 
  {
    if (this.readyState == 4 && this.status == 200) 
    {
		var doc = document.createElement( 'html' );
		doc.innerHTML = xhr.responseText;
		return doc;
    }
  };  
  xhr.open("GET", url, false);
  xhr.send();
  return xhr.onreadystatechange();
}

var task_q = [start];
var done_q = [];

while (task_q.length > 0)
{
	var doc = getDocumentXml(task_q[0]);
	done_q.push(task_q[0]);
	task_q.splice(0, 1);
	
	if (doc.getElementsByTagName("font").length > 0) 
		console.log(doc.getElementsByTagName("font")[0].innerText.substring(15));
		
	var hrefs = doc.getElementsByTagName("a");
	
	for (var idx = 0; idx < hrefs.length; idx++)
	{
		if (!task_q.includes(hrefs[idx].href) && !done_q.includes(hrefs[idx].href)) 
			task_q.push(hrefs[idx].href);
	}	
}
