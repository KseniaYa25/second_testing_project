from faker import Faker
import json

fake = Faker()

class DeviceBuilder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.device_data = {
            "name": "",
            "data": {}
        }
        return self
    
    def with_name(self, name: str = None):
        if name is None:
            brands = ["Apple", "Samsung", "Dell", "HP", "Lenovo", "Asus"]
            models = ["MacBook Pro", "Galaxy Book", "XPS", "Pavilion", "ThinkPad", "ZenBook"]
            sizes = ["13", "14", "15", "16"]
            name = f"{fake.random_element(brands)} {fake.random_element(models)} {fake.random_element(sizes)}"
        
        self.device_data["name"] = name
        return self
    
    def with_year(self, year: int = None):
        if year is None:
            year = fake.random_int(min=1990, max=2024)
        self.device_data["data"]["year"] = year
        return self
    
    def with_price(self, price: float = None):
        if price is None:
            price = round(fake.random.uniform(500, 3000), 2)
        self.device_data["data"]["price"] = price
        return self
    
    def with_cpu(self, cpu: str = None):
        if cpu is None:
            cpus = ["Intel Core i5", "Intel Core i7", "Intel Core i9", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1", "Apple M2"]
            cpu = fake.random_element(cpus)
        self.device_data["data"]["CPU model"] = cpu
        return self
    
    def with_disk_size(self, size: str = None):
        if size is None:
            sizes = ["256 GB", "512 GB", "1 TB", "2 TB"]
            size = fake.random_element(sizes)
        self.device_data["data"]["Hard disk size"] = size
        return self
    
    def with_color(self, color: str = None):
        if color is None:
            colors = ["silver", "space gray", "gold", "black", "white"]
            color = fake.random_element(colors)
        self.device_data["data"]["color"] = color
        return self
    
    def build(self):
        return self.device_data.copy()
    
    def build_json(self):
        return json.dumps(self.device_data, indent=2)