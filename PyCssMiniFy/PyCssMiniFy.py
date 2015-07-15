# -*- coding: utf-8 -*-

def minify_css(file_path):
	if type(file_path)!=str :
		raise Exception("Image file path must be string")
	
	if not os.path.isfile(os.path.abspath(file_path)) and not os.path.isdir(os.path.abspath(file_path)):
		raise Exception("file path must be a valid directory or a file path "+os.path.abspath(file_path) )
		
	if os.path.isfile(file_path) and os.path.getsize(file_path)>>20 < 5:
		
		files={'input':open(file_path,'r')}			
		r=requests.post("http://cssminifier.com/raw",files=files,stream=True)
		if r.status_code == 200:
     			with open(file_path.rstrip(".css")+".min.css", 'w') as f:
        			for chunk in r.iter_content(1024):
            				f.write(chunk)
            	
        elif os.path.isdir(file_path):
        	for root,dirs,files in os.walk("."):
			for file in files:
				if file.endswith(".css") and not file.endswith(".min.css"):
					 minify_css(os.path.abspath(os.path.join(root,file)))

def minify(file_path):
	with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
		for root,dirs,files in os.walk(file_path):
		    for file in files:
		        if file.endswith(".css") and not file.endswith(".min.css"):
		            executor.submit(minify_css,file_path)

