

class NK_InputLatentsText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["txt2img", "img2img", "inpaint"],),
                "txt2img": ("LATENT",),
                "img2img": ("LATENT",),
                "inpaint": ("LATENT",)
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = True
    FUNCTION = "InputLatentsText"

    CATEGORY = "image"

    def InputLatentsText(self, Input, txt2img, img2img, inpaint):
        if Input == "txt2img":
            return (txt2img, )
        elif Input == "img2img":
            return (img2img, )
        else:
            return (inpaint, )             
            
NODE_CLASS_MAPPINGS = {
    "NK_InputLatentsText": NK_InputLatentsText
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NK_InputLatentsText": "NK 3way Switch"
}