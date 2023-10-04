


class NK_ImageInputSwitch_4way_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
         return {
            "required": {
                "Input": (["openpose", "depth", "canny", "normal"],),
            },
            "optional": {               
               "openpose": ("IMAGE",),
                "depth": ("IMAGE",),
				"canny": ("IMAGE",),
                "normal": ("IMAGE",)
            }
        }


    RETURN_TYPES = ("IMAGE",)
    OUTPUT_NODE = True
    FUNCTION = "InputImages_4"

    CATEGORY = "image"

    def InputImages_4(self, Input="normal", openpose=None, depth=None, canny=None, normal=None):
        if Input == "openpose":
            return (openpose, )
        elif Input == "depth":
            return (depth, )
        elif Input == "canny":
            return (canny, )			
        else:
            return (normal, ) 

NODE_CLASS_MAPPINGS = {
    "NK_ImageInputSwitch_4way_v2": NK_ImageInputSwitch_4way_v2
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NK_ImageInputSwitch_4way_v2": "NK 4way Image Swtich v2"
}