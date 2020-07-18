class Converter():
    def __init__(self):
        # 1.335 billion cubic km
        # 361 hundred million square km
        # 1.5 qunitillion tons
        self.metrics = {"volume": int(1.335e9), "area": int(361e8), "mass": int(1.5e18)}
        self.conversions = [{"cubic km": 1, "cup": int(4.23e12), "liter": int(1e12), "cubic mile": 0.24}, {"square km": 1, "square mile": 0.386}, {"ton": 1}]
        self.unitIndex = {"volume": 0, "area": 1, "mass": 2}
    def convert(self, metric, unit):
        return self.metrics.get(metric) * self.conversions[self.unitIndex.get(metric)].get(unit)

converter = Converter()
