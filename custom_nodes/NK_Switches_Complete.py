


class NK_AspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "width": ("INT", {"default": 64, "min": 64, "max": 2048,}),
                    "height": ("INT", {"default": 64, "min": 64, "max": 2048}),
                    "aspectRatio": ([
                    "custom",
                    "1:1  - 1024x1024 square", 
                    "3:4  - 896x1152 portrait", 
                    "2:3  - 832x1216 portrait", 
                    "5:8  - 768x1216 portrait", 
                    "9:16 - 768x1344 portrait", 
                    "9:19 - 704x1472 portrait", 
                    "9:21 - 640x1536 portrait", 
                    "4:3  - 1152x896 landscape",                     
                    "3:2  - 1216x832 landscape",                     
                    "8:5  - 1216x768 landscape", 
                    "16:9 - 1344x768 landscape", 
                    "19:9 - 1472x704 landscape", 
                    "21:9 - 1536x640 landscape",
                    "1:1  - 512x512 square",
                    "3:4  - 512x682 portrait",
                    "2:3  - 512x768 portrait",
                    "5:8  - 512x819 portrait",
                    "9:16 - 512x910 portrait",
                    "4:3  - 768x512 landscape",
                    "3:2  - 682x512 landscape",
                    "8:5  - 819x512 landscape",
                    "16:9 - 910x512 landscape"],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "SDXL_AspectRatio"
    CATEGORY = "NK-Switches"

    def SDXL_AspectRatio(self, width, height, aspectRatio):
        if aspectRatio == "1:1  - 1024x1024 square":
            width, height = 1024, 1024
        elif aspectRatio == "3:4  - 896x1152 portrait":
            width, height = 896, 1152            
        elif aspectRatio == "2:3  - 832x1216 portrait":
            width, height = 832, 1216
        elif aspectRatio == "5:8  - 768x1216 portrait":
            width, height = 768, 1216
        elif aspectRatio == "9:16 - 768x1344 portrait":
            width, height = 768, 1344
        elif aspectRatio == "9:19 - 704x1472 portrait":
            width, height = 704, 1472
        elif aspectRatio == "9:21 - 640x1536 portrait":
            width, height = 640, 1536
        elif aspectRatio == "4:3  - 1152x896 landscape":
            width, height = 1152, 896            
        elif aspectRatio == "3:2  - 1216x832 landscape":
            width, height = 1216, 832
        elif aspectRatio == "8:5  - 1216x768 landscape":
            width, height = 1216, 768
        elif aspectRatio == "16:9 - 1344x768 landscape":
            width, height = 1344, 768
        elif aspectRatio == "19:9 - 1472x704 landscape":
            width, height = 1472, 704
        elif aspectRatio == "21:9 - 1536x640 landscape":
            width, height = 1536, 640
        elif aspectRatio == "1:1  - 512x512 square":
            width, height = 512, 512
        elif aspectRatio == "3:4  - 512x682 portrait":
            width, height = 512, 682
        elif aspectRatio == "2:3  - 512x768 portrait":
            width, height = 512, 768
        elif aspectRatio == "5:8  - 512x819 portrait":
            width, height = 512, 819
        elif aspectRatio == "9:16 - 512x910 portrait":
            width, height = 512, 910    
        elif aspectRatio == "4:3  - 682x512 landscape":
            width, height = 682, 512
        elif aspectRatio == "3:2  - 768x512 landscape":
            width, height = 768, 512
        elif aspectRatio == "8:5  - 819x512 landscape":
            width, height = 819, 512
        elif aspectRatio == "16:9 - 910x512 landscape":
            width, height = 910, 512    
        return(width, height)

########

class NK_ConditioningInputSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["condition_1", "condition_2"],),
                "condition_1": ("CONDITIONING",),
                "condition_2": ("CONDITIONING",)
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    OUTPUT_NODE = True
    FUNCTION = "InputConditioning"

    CATEGORY = "NK-Switches"

    def InputConditioning(self, Input, condition_1, condition_2):
        if Input == "condition_1":
            return (condition_1, )
        else:
            return (condition_2, )  

########

class NK_ImageInputSwitch4way:
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

    CATEGORY = "NK-Switches"

    def InputImages_4(self, Input="normal", openpose=None, depth=None, canny=None, normal=None):
        if Input == "openpose":
            return (openpose, )
        elif Input == "depth":
            return (depth, )
        elif Input == "canny":
            return (canny, )			
        else:
            return (normal, ) 

########

class NK_ImageInputSwitch4way_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
         return {
            "required": {
                "Input": (["img_1", "img_2", "img_3", "img_4"],),
            },
            "optional": {               
               "img_1": ("IMAGE",),
                "img_2": ("IMAGE",),
				"img_3": ("IMAGE",),
                "img_4": ("IMAGE",)
            }
        }


    RETURN_TYPES = ("IMAGE",)
    OUTPUT_NODE = True
    FUNCTION = "InputImages_4"

    CATEGORY = "NK-Switches"
    
    def InputImages_4(self, Input="normal", img_1=None, img_2=None, img_3=None, img_4=None):
        if Input == "img_1":
            return (img_1, )
        elif Input == "img 2":
            return (img_2, )
        elif Input == "img_3":
            return (img_3, )			
        else:
            return (img_4, ) 

########

class NK_InputLatents4Way:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["txt2img", "img2img", "inpaint", "controlnet"],),
                },
            "optional": { 
                "txt2img": ("LATENT",),
                "img2img": ("LATENT",),
                "inpaint": ("LATENT",),
                "controlnet":("LATENT",)
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = True
    FUNCTION = "NK_InputLatents4Way"

    CATEGORY = "NK-Switches"

    def NK_InputLatents4Way(self, Input="normal", txt2img=None, img2img=None, inpaint=None, controlnet=None):
        if Input == "txt2img":
            return (txt2img, )
        elif Input == "img2img":
            return (img2img, )
        elif Input == "inpaint":
            return (inpaint, )
        else:
            return (controlnet, ) 

########

class NK_InputLatents4Way_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["latent_1", "latent_2", "latent_3", "latent_4"],),
                },
            "optional": { 
                "latent_1": ("LATENT",),
                "latent_2": ("LATENT",),
                "latent_3": ("LATENT",),
                "latent_4":("LATENT",)
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = True
    FUNCTION = "NK_InputLatents4Way_v2"

    CATEGORY = "NK-Switches"
    
    def NK_InputLatents4Way_v2(self, Input="normal", latent_1=None, latent_2=None, latent_3=None, latent_4=None):
        if Input == "latent_1":
            return (latent_1, )
        elif Input == "latent_2":
            return (latent_2, )
        elif Input == "latent_3":
            return (latent_3, )
        else:
            return (latent_4, )      

########

class NK_InputLatents3way:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["txt2img", "img2img", "inpaint"],),
                },
            "optional": { 
                "txt2img": ("LATENT",),
                "img2img": ("LATENT",),
                "inpaint": ("LATENT",)
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = True
    FUNCTION = "InputLatentsText"

    CATEGORY = "NK-Switches"

    def InputLatentsText(self, Input="normal", txt2img=None, img2img=None, inpaint=None):
        if Input == "txt2img":
            return (txt2img, )
        elif Input == "img2img":
            return (img2img, )
        else:
            return (inpaint, ) 

########

class NK_InputLatents3way_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": (["latent_1", "latent_2", "latent_3"],),
                },
            "optional": { 
                "latent_1": ("LATENT",),
                "latent_2": ("LATENT",),
                "latent_3": ("LATENT",)
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = True
    FUNCTION = "InputLatentsText"

    CATEGORY = "NK-Switches"

    def InputLatentsText(self, Input="normal", latent_1=None, latent_2=None, latent_3=None):
        if Input == "latent_1":
            return (latent_1, )
        elif Input == "latent_2":
            return (latent_2, )
        else:
            return (latent_3, ) 

#########

class NK_ModelInputSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
         return {
            "required": {
                "Input": (["Model", "FreeU"],),
            },
            "optional": {               
                "Model": ("MODEL",),
                "FreeU": ("MODEL",)
            }
        }

    RETURN_TYPES = ("MODEL",)
    OUTPUT_NODE = True
    FUNCTION = "InputModel"

    CATEGORY = "NK-Switches"

    def InputModel(self, Input="normal", Model=None, FreeU=None):
        if Input == "Model":
            return (Model, )	
        else:
            return (FreeU, ) 

########

class NK_ModelInputSwitch3Way:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
         return {
            "required": {
                "Input": (["Model", "FreeU_1", "FreeU_2"],),
            },
            "optional": {               
                "Model": ("MODEL",),
                "FreeU_1": ("MODEL",),
				"FreeU_2": ("MODEL",)
            }
        }

    RETURN_TYPES = ("MODEL",)
    OUTPUT_NODE = True
    FUNCTION = "InputModel"

    CATEGORY = "NK-Switches"

    def InputModel(self, Input="normal", Model=None, FreeU_1=None, FreeU_2=None):
        if Input == "Model":
            return (Model, )
        elif Input == "FreeU_1":
            return (FreeU_1, )		
        else:
            return (FreeU_2, ) 

########

class NK_ModelInputSwitch4Way:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
         return {
            "required": {
                "Input": (["Model", "FreeU_1", "FreeU_2", "FreeU_3"],),
            },
            "optional": {               
                "Model": ("MODEL",),
                "FreeU_1": ("MODEL",),
				"FreeU_2": ("MODEL",),
                "FreeU_3": ("MODEL",)
            }
        }

    RETURN_TYPES = ("MODEL",)
    OUTPUT_NODE = True
    FUNCTION = "InputModel"

    CATEGORY = "NK-Switches"

    def InputModel(self, Input="normal", Model=None, FreeU_1=None, FreeU_2=None, FreeU_3=None):
        if Input == "Model":
            return (Model, )
        elif Input == "FreeU_1":
            return (FreeU_1, )
        elif Input == "FreeU_2":
            return (FreeU_2, )			
        else:
            return (FreeU_3, ) 

########

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

    CATEGORY = "NK-Switches"

    def InputVAE(self, Input, baked, option):
        if Input == "baked":
            return (baked, )
        else:
            return (option, )             
            
NODE_CLASS_MAPPINGS = {
    "NK_AspectRatio": NK_AspectRatio,
    "NK_ConditioningInputSwitch": NK_ConditioningInputSwitch,
    "NK_ImageInputSwitch4way": NK_ImageInputSwitch4way,
    "NK_ImageInputSwitch4way_v2": NK_ImageInputSwitch4way_v2,
    "NK_InputLatents4Way": NK_InputLatents4Way,
    "NK_InputLatents4Way_v2": NK_InputLatents4Way_v2,
    "NK_InputLatents3way": NK_InputLatents3way,
    "NK_InputLatents3way_v2": NK_InputLatents3way_v2,
    "NK_ModelInputSwitch": NK_ModelInputSwitch,
    "NK_ModelInputSwitch3Way": NK_ModelInputSwitch3Way,
    "NK_ModelInputSwitch4Way": NK_ModelInputSwitch4Way,
    "NK_VAESwitch": NK_VAESwitch,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NK_AspectRatio": "NK Aspect Ratio",
    "NK_ConditioningInputSwitch": "NK Conditioning Switch",
    "NK_ImageInputSwitch4way": "NK 4way Image Swtich",
    "NK_ImageInputSwitch4way_v2": "NK 4way Image Swtich v2",
    "NK_InputLatents4Way": "NK 4way Switch",
    "NK_InputLatents4Way_v2": "NK 4way Switch v2",
    "NK_InputLatents3way": "NK 3way Switch",
    "NK_InputLatents3way_v2": "NK 3way Switch_v2",
    "NK_ModelInputSwitch": "NK Model Input Switch",
    "NK_ModelInputSwitch3Way": "NK Model Input Switch 3Way",
    "NK_ModelInputSwitch4Way": "NK Model Input Switch 4Way",
    "NK_VAESwitch": "NK VAE Switch",
}