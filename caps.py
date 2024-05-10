import numpy as np

class MosCaps:
    def __init__(self, gm: float, ft: float) -> None:
        cgg = gm / (2*np.pi*ft)
        self.caps = {
            "cgg": 0.0,
            "cgd": 0.0,
            "cdd": 0.0,
            "cdb": 0.0,
            "cgs": 0.0
        }
        for cap in self.caps:
            match cap:
                case "cgg":
                    self.caps[cap] = cgg
                case "cgd":
                    self.caps[cap] = 0.24*cgg
                case "cdd":
                    self.caps[cap] = 0.6*cgg
                case "cdb":
                    self.caps[cap] = self.caps["cdd"] - self.caps["cgd"]
                case "cgs":
                    # actually cgs + cgb
                    # neglect cgb
                    self.caps[cap] = self.caps["cgg"] - self.caps["cgd"]
    def cgg(self):
        return self.caps["cgg"]
    def cgd(self):
        return self.caps["cgd"]
    def cdd(self):
        return self.caps["cdd"]
    def cdb(self):
        return self.caps["cdb"]
    def cgs(self):
        return self.caps["cgs"]