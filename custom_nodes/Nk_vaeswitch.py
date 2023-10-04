


class NK_VAESwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["baked", "option"],),
                "baked": ("VAE",),
                "option": ("VAE",)              
            }
        }

    RETURN_TYPES = ("VAE",)
    OUTPUT_NODE = True
    FUNCTION = "InputVAE"

    CATEGORY = "image"

    def InputVAE(self, Input, baked, option):
        if Input == "baked":
            return (baked, )
        else:
            return (option, )             
            
NODE_CLASS_MAPPINGS = {
    "NK_VAESwitch": NK_VAESwitch
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NK_VAESwitch": "NK VAE Switch"
}