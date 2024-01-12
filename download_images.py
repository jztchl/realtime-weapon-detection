from simple_image_download import simple_image_download as simp

response = simp.simple_image_download
keywords =["guns","knife"]
for k in keywords:
    response().download(k,200)