

class NK_InputLatents4Way:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["txt2img", "img2img", "inpaint", "controlnet"],),
                "txt2img": ("LATENT",),
                "img2img": ("LATENT",),
                "inpaint": ("LATENT",),
                "controlnet":("LATENT",)
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = True
    FUNCTION = "NK_InputLatents4Way"

    CATEGORY = "image"

    def NK_InputLatents4Way(self, Input, txt2img, img2img, inpaint, controlnet):
        if Input == "txt2img":
            return (txt2img, )
        elif Input == "img2img":
            return (img2img, )
        elif Input == "inpaint":
            return (inpaint, )
        else:
            return (controlnet, )             
            
NODE_CLASS_MAPPINGS = {
    "NK_InputLatents4Way": NK_InputLatents4Way
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NK_InputLatents4Way": "NK 4way Switch"
}