from django.db import models  # type: ignore
import uuid


# Base model for shared attributes
class BaseProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, help_text="Price in BDT"
    )
    regular_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Regular price in BDT",
    )
    brand = models.CharField(
        max_length=50, blank=True, null=True, help_text="Brand of the product"
    )
    model = models.CharField(
        max_length=100, blank=True, null=True, help_text="Model name of the product"
    )
    warranty = models.CharField(
        max_length=50,
        choices=[
            ("1 Year", "1 Year"),
            ("2 Years", "2 Years"),
            ("3 Years", "3 Years"),
            ("4 Years", "4 Years"),
            ("5 Years", "5 Years"),
            ("10 Years", "10 Years"),
            ("Lifetime Warranty", "Lifetime Warranty"),
        ],
        blank=True,
        null=True,
        help_text="Warranty duration",
    )
    description = models.TextField(blank=True, help_text="Description of the product")
    category = models.CharField(
        max_length=50,
        choices=[
            ("CPU", "CPU"),
            ("Cooler", "Cooler"),
            ("Motherboard", "Motherboard"),
            ("RAM", "RAM"),
            ("SSD", "SSD"),
            ("HDD", "HDD"),
            ("GPU", "GPU"),
            ("Power Supply", "Power Supply"),
            ("Casing", "Casing"),
            ("Monitor", "Monitor"),
            ("Keyboard", "Keyboard"),
            ("Mouse", "Mouse"),
            ("Headphone", "Headphone"),
        ],
        blank=True,
        null=True,
        help_text="Category of the product",
    )
    tdp = models.IntegerField(
        blank=True, null=True, help_text="Thermal Design Power (TDP) in watts"
    )

    class Meta:
        abstract = True  # This model won't be created as a table


"""
Core Components:
1. CPU
2. Cooler
3. Motherboard
4. RAM
5. SSD
6. HDD
7. GPU
8. Power Supply
9. Casing
"""


class CPU(BaseProduct):
    image1 = models.ImageField(
        upload_to="cpu_images/",
        blank=True,
        null=True,
        help_text="Image of the CPU (main)",
    )
    image2 = models.ImageField(
        upload_to="cpu_images/",
        blank=True,
        null=True,
        help_text="Image of the CPU (optional)",
    )
    image3 = models.ImageField(
        upload_to="cpu_images/",
        blank=True,
        null=True,
        help_text="Image of the CPU (optional)",
    )
    image4 = models.ImageField(
        upload_to="cpu_images/",
        blank=True,
        null=True,
        help_text="Image of the CPU (optional)",
    )
    image5 = models.ImageField(
        upload_to="cpu_images/",
        blank=True,
        null=True,
        help_text="Image of the CPU (optional)",
    )
    socket = models.CharField(
        max_length=50,
        choices=[
            ("LGA 1200", "LGA 1200"),
            ("LGA 1700", "LGA 1700"),
            ("LGA 1851", "LGA 1851"),
            ("AM4", "AM4"),
            ("AM5", "AM5"),
            ("TR4", "TR4"),
        ],
        blank=True,
        null=True,
        help_text="Socket",
    )
    cores = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of CPU cores",
    )
    threads = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of threads",
    )
    base_frequency = models.FloatField(
        blank=True, null=True, help_text="Base frequency in GHz"
    )
    boost_frequency = models.FloatField(
        blank=True, null=True, help_text="Boost frequency in GHz"
    )
    cache = models.IntegerField(blank=True, null=True, help_text="Cache size in MB")
    processor_graphics = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Integrated graphics (e.g., Intel UHD)",
    )

    class Meta:
        verbose_name = "CPU"
        verbose_name_plural = "CPUs"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.cores}C/{self.threads}T) {self.boost_frequency} GHz"


class Cooler(BaseProduct):
    image1 = models.ImageField(
        upload_to="cooler_images/",
        blank=True,
        null=True,
        help_text="Image of the Cooler (main)",
    )
    image2 = models.ImageField(
        upload_to="cooler_images/",
        blank=True,
        null=True,
        help_text="Image of the Cooler (optional)",
    )
    image3 = models.ImageField(
        upload_to="cooler_images/",
        blank=True,
        null=True,
        help_text="Image of the Cooler (optional)",
    )
    image4 = models.ImageField(
        upload_to="cooler_images/",
        blank=True,
        null=True,
        help_text="Image of the Cooler (optional)",
    )
    image5 = models.ImageField(
        upload_to="cooler_images/",
        blank=True,
        null=True,
        help_text="Image of the Cooler (optional)",
    )
    cooler_type = models.CharField(
        max_length=50,
        choices=[
            ("Air Cooler", "Air Cooler"),
            ("Liquid Cooler", "Liquid Cooler"),
        ],
        blank=True,
        null=True,
        help_text="Cooler Type",
    )
    cooler_size = models.CharField(
        max_length=50,
        choices=[
            ("120 mm", "120 mm"),
            ("140 mm", "140 mm"),
            ("240 mm", "240 mm"),
            ("280 mm", "280 mm"),
            ("360 mm", "360 mm"),
            ("420 mm", "420 mm"),
            ("480 mm", "480 mm"),
        ],
        blank=True,
        null=True,
        help_text="Cooler size",
    )
    fan_speed = models.IntegerField(
        blank=True,
        null=True,
        help_text="Fan speed in RPM",
    )
    noise_level = models.IntegerField(
        blank=True,
        null=True,
        help_text="Noise level in dB",
    )
    rgb = models.BooleanField(
        blank=True,
        null=True,
        help_text="RGB lighting",
    )
    tdp = models.IntegerField(
        blank=True,
        null=True,
        help_text="Thermal Design Power (TDP) in watts",
    )

    class Meta:
        verbose_name = "Cooler"
        verbose_name_plural = "Coolers"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.cooler_type})"


class Motherboard(BaseProduct):
    image1 = models.ImageField(
        upload_to="motherboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Motherboard (main)",
    )
    image2 = models.ImageField(
        upload_to="motherboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Motherboard (optional)",
    )
    image3 = models.ImageField(
        upload_to="motherboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Motherboard (optional)",
    )
    image4 = models.ImageField(
        upload_to="motherboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Motherboard (optional)",
    )
    image5 = models.ImageField(
        upload_to="motherboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Motherboard (optional)",
    )
    form_factor = models.CharField(
        max_length=50,
        choices=[
            ("ATX", "ATX"),
            ("Micro-ATX", "Micro-ATX"),
            ("Mini-ITX", "Mini-ITX"),
            ("E-ATX", "E-ATX"),
        ],
        blank=True,
        null=True,
        help_text="Form factor",
    )
    socket = models.CharField(
        max_length=50,
        choices=[
            ("LGA 1200", "LGA 1200"),
            ("LGA 1700", "LGA 1700"),
            ("LGA 1851", "LGA 1851"),
            ("AM4", "AM4"),
            ("AM5", "AM5"),
            ("TR4", "TR4"),
        ],
        blank=True,
        null=True,
        help_text="Socket",
    )
    chipset = models.CharField(
        max_length=50,
        choices=[
            ("H510", "H510"),
            ("B460", "B460"),
            ("H610", "H610"),
            ("B660", "B660"),
            ("B760", "B760"),
            ("Z790", "Z790"),
            ("Z890", "Z890"),
            ("A520", "A520"),
            ("B450", "B450"),
            ("B550", "B550"),
            ("X570", "X570"),
            ("A620", "A620"),
            ("B650", "B650"),
            ("X670", "X670"),
            ("X670E", "X670E"),
            ("X870", "X870"),
            ("X870E", "X870E"),
            ("TRX40", "TRX40"),
        ],
        blank=True,
        null=True,
        help_text="Chipset",
    )
    memory_slots = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of memory slots",
    )
    memory_type = models.CharField(
        max_length=50,
        choices=[
            ("DDR4", "DDR4"),
            ("DDR5", "DDR5"),
        ],
        help_text="Type of RAM",
    )
    max_memory = models.CharField(
        max_length=10,
        choices=[
            ("32 GB", "32 GB"),
            ("64 GB", "64 GB"),
            ("128 GB", "128 GB"),
            ("256 GB", "256 GB"),
            ("512 GB", "512 GB"),
            ("1 TB", "1 TB"),
            ("2 TB", "2 TB"),
        ],
        blank=True,
        null=True,
        help_text="Maximum memory capacity",
    )
    pcie_slots = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of PCIe slots",
    )
    m2_slots = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of M.2 slots",
    )
    sata_ports = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of SATA ports",
    )
    usb_ports = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of USB ports",
    )
    wifi_bluetooth = models.BooleanField(
        blank=True,
        null=True,
        help_text="Wi-Fi and Bluetooth support",
    )

    class Meta:
        verbose_name = "Motherboard"
        verbose_name_plural = "Motherboards"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.socket}) {self.chipset} {self.form_factor}"


class RAM(BaseProduct):
    image1 = models.ImageField(
        upload_to="ram_images/",
        blank=True,
        null=True,
        help_text="Image of the RAM (main)",
    )
    image2 = models.ImageField(
        upload_to="ram_images/",
        blank=True,
        null=True,
        help_text="Image of the RAM (optional)",
    )
    image3 = models.ImageField(
        upload_to="ram_images/",
        blank=True,
        null=True,
        help_text="Image of the RAM (optional)",
    )
    image4 = models.ImageField(
        upload_to="ram_images/",
        blank=True,
        null=True,
        help_text="Image of the RAM (optional)",
    )
    image5 = models.ImageField(
        upload_to="ram_images/",
        blank=True,
        null=True,
        help_text="Image of the RAM (optional)",
    )
    ram_class = models.CharField(
        max_length=50,
        choices=[
            ("Desktop", "Desktop"),
            ("Laptop", "Laptop"),
            ("Server", "Server"),
        ],
        blank=True,
        null=True,
        help_text="Type of RAM",
    )
    ram_type = models.CharField(
        max_length=50,
        choices=[
            ("DDR3", "DDR3"),
            ("DDR4", "DDR4"),
            ("DDR5", "DDR5"),
            ("LPDDR3", "LPDDR3"),
            ("LPDDR4", "LPDDR4"),
            ("LPDDR5", "LPDDR5"),
            ("ECC DDR4", "ECC DDR4"),
            ("ECC DDR5", "ECC DDR5"),
        ],
        help_text="Type of RAM",
    )
    memory_capacity = models.CharField(
        max_length=10,
        choices=[
            ("4 GB", "4 GB"),
            ("8 GB", "8 GB"),
            ("16 GB", "16 GB"),
            ("32 GB", "32 GB"),
            ("64 GB", "64 GB"),
        ],
        blank=True,
        null=True,
        help_text="RAM capacity",
    )
    frequency = models.CharField(
        max_length=50,
        choices=[
            ("1333 MHz", "1333 MHz"),
            ("1600 MHz", "1600 MHz"),
            ("1866 MHz", "1866 MHz"),
            ("2133 MHz", "2133 MHz"),
            ("2400 MHz", "2400 MHz"),
            ("2666 MHz", "2666 MHz"),
            ("3000 MHz", "3000 MHz"),
            ("3200 MHz", "3200 MHz"),
            ("3600 MHz", "3600 MHz"),
            ("4000 MHz", "4000 MHz"),
            ("4266 MHz", "4266 MHz"),
            ("4400 MHz", "4400 MHz"),
            ("4600 MHz", "4600 MHz"),
            ("4800 MHz", "4800 MHz"),
            ("5000 MHz", "5000 MHz"),
            ("5200 MHz", "5200 MHz"),
            ("5400 MHz", "5400 MHz"),
            ("5600 MHz", "5600 MHz"),
            ("5800 MHz", "5800 MHz"),
            ("6000 MHz", "6000 MHz"),
            ("6400 MHz", "6400 MHz"),
            ("6800 MHz", "6800 MHz"),
            ("7200 MHz", "7200 MHz"),
            ("7400 MHz", "7400 MHz"),
            ("7600 MHz", "7600 MHz"),
            ("7800 MHz", "7800 MHz"),
            ("8000 MHz", "8000 MHz"),
        ],
        blank=True,
        null=True,
        help_text="Frequency",
    )

    class Meta:
        verbose_name = "RAM"
        verbose_name_plural = "RAMs"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.memory_capacity}) {self.ram_type}"


class SSD(BaseProduct):
    image1 = models.ImageField(
        upload_to="ssd_images/",
        blank=True,
        null=True,
        help_text="Image of the SSD (main)",
    )
    image2 = models.ImageField(
        upload_to="ssd_images/",
        blank=True,
        null=True,
        help_text="Image of the SSD (optional)",
    )
    image3 = models.ImageField(
        upload_to="ssd_images/",
        blank=True,
        null=True,
        help_text="Image of the SSD (optional)",
    )
    image4 = models.ImageField(
        upload_to="ssd_images/",
        blank=True,
        null=True,
        help_text="Image of the SSD (optional)",
    )
    image5 = models.ImageField(
        upload_to="ssd_images/",
        blank=True,
        null=True,
        help_text="Image of the SSD (optional)",
    )
    storage_capacity = models.CharField(
        max_length=10,
        choices=[
            ("120 GB", "120 GB"),
            ("240 GB", "240 GB"),
            ("256 GB", "256 GB"),
            ("480 GB", "480 GB"),
            ("512 GB", "512 GB"),
            ("1 TB", "1 TB"),
            ("2 TB", "2 TB"),
            ("4 TB", "4 TB"),
            ("8 TB", "8 TB"),
        ],
        blank=True,
        null=True,
        help_text="Storage capacity",
    )
    form_factor = models.CharField(
        max_length=50,
        choices=[
            ("2.5-inch", "2.5-inch"),
            ("M.2", "M.2"),
            ("PCIe Add-in Card", "PCIe Add-in Card"),
        ],
        blank=True,
        null=True,
        help_text="Form factor",
    )
    interface = models.CharField(
        max_length=50,
        choices=[
            ("SATA III", "SATA III"),
            ("PCIe 3.0 x4", "PCIe 3.0 x4"),
            ("PCIe 4.0 x4", "PCIe 4.0 x4"),
            ("PCIe 4.0 x8", "PCIe 4.0 x8"),
        ],
        blank=True,
        null=True,
        help_text="Interface",
    )
    read_speed = models.IntegerField(
        blank=True, null=True, help_text="Read speed in MB/s"
    )
    write_speed = models.IntegerField(
        blank=True, null=True, help_text="Write speed in MB/s"
    )

    class Meta:
        verbose_name = "SSD"
        verbose_name_plural = "SSDs"

    def __str__(self):
        return f"{self.brand} {self.model}"


class HDD(BaseProduct):
    image1 = models.ImageField(
        upload_to="hdd_images/",
        blank=True,
        null=True,
        help_text="Image of the HDD (main)",
    )
    image2 = models.ImageField(
        upload_to="hdd_images/",
        blank=True,
        null=True,
        help_text="Image of the HDD (optional)",
    )
    image3 = models.ImageField(
        upload_to="hdd_images/",
        blank=True,
        null=True,
        help_text="Image of the HDD (optional)",
    )
    image4 = models.ImageField(
        upload_to="hdd_images/",
        blank=True,
        null=True,
        help_text="Image of the HDD (optional)",
    )
    image5 = models.ImageField(
        upload_to="hdd_images/",
        blank=True,
        null=True,
        help_text="Image of the HDD (optional)",
    )
    storage_capacity = models.CharField(
        max_length=10,
        choices=[
            ("500 GB", "500 GB"),
            ("1 TB", "1 TB"),
            ("2 TB", "2 TB"),
            ("4 TB", "4 TB"),
            ("6 TB", "6 TB"),
            ("8 TB", "8 TB"),
            ("10 TB", "10 TB"),
            ("12 TB", "12 TB"),
            ("14 TB", "14 TB"),
            ("16 TB", "16 TB"),
            ("18 TB", "18 TB"),
        ],
        blank=True,
        null=True,
        help_text="Storage capacity",
    )
    form_factor = models.CharField(
        max_length=50,
        choices=[
            ("2.5-inch", "2.5-inch"),
            ("3.5-inch", "3.5-inch"),
        ],
        blank=True,
        null=True,
        help_text="Form factor",
    )
    interface = models.CharField(
        max_length=50,
        choices=[
            ("SATA II", "SATA II"),
            ("SATA III", "SATA III"),
        ],
        blank=True,
        null=True,
        help_text="Interface",
    )
    rpm = models.CharField(
        max_length=50,
        choices=[
            ("5400 RPM", "5400 RPM"),
            ("7200 RPM", "7200 RPM"),
        ],
        blank=True,
        null=True,
        help_text="Rotational speed",
    )
    cache = models.IntegerField(blank=True, null=True, help_text="Cache size in MB")

    class Meta:
        verbose_name = "HDD"
        verbose_name_plural = "HDDs"

    def __str__(self):
        return f"{self.brand} {self.model}"


class GPU(BaseProduct):
    image1 = models.ImageField(
        upload_to="gpu_images/",
        blank=True,
        null=True,
        help_text="Image of the GPU (main)",
    )
    image2 = models.ImageField(
        upload_to="gpu_images/",
        blank=True,
        null=True,
        help_text="Image of the GPU (optional)",
    )
    image3 = models.ImageField(
        upload_to="gpu_images/",
        blank=True,
        null=True,
        help_text="Image of the GPU (optional)",
    )
    image4 = models.ImageField(
        upload_to="gpu_images/",
        blank=True,
        null=True,
        help_text="Image of the GPU (optional)",
    )
    image5 = models.ImageField(
        upload_to="gpu_images/",
        blank=True,
        null=True,
        help_text="Image of the GPU (optional)",
    )
    memory_type = models.CharField(
        max_length=50,
        choices=[
            ("DDR3", "DDR3"),
            ("GDDR5", "GDDR5"),
            ("GDDR5X", "GDDR5X"),
            ("GDDR6", "GDDR6"),
            ("GDDR6X", "GDDR6X"),
        ],
        blank=True,
        null=True,
        help_text="Type of GPU memory",
    )
    vram_capacity = models.CharField(
        max_length=10,
        choices=[
            ("2 GB", "2 GB"),
            ("4 GB", "4 GB"),
            ("6 GB", "6 GB"),
            ("8 GB", "8 GB"),
            ("12 GB", "12 GB"),
            ("16 GB", "16 GB"),
            ("24 GB", "24 GB"),
            ("32 GB", "32 GB"),
        ],
        blank=True,
        null=True,
        help_text="VRAM capacity",
    )
    max_resolution = models.CharField(
        max_length=50, blank=True, null=True, help_text="Max supported resolution"
    )
    core_clock = models.FloatField(
        blank=True, null=True, help_text="Core clock speed in MHz"
    )
    memory_clock = models.FloatField(
        blank=True, null=True, help_text="Memory clock speed in MHz"
    )
    cores = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of GPU cores",
    )
    memory_bus = models.CharField(
        max_length=50,
        choices=[
            ("64-bit", "64-bit"),
            ("128-bit", "128-bit"),
            ("192-bit", "192-bit"),
            ("256-bit", "256-bit"),
            ("384-bit", "384-bit"),
            ("448-bit", "448-bit"),
            ("512-bit", "512-bit"),
        ],
        blank=True,
        null=True,
        help_text="Memory bus width",
    )
    memory_interface = models.CharField(
        max_length=20,
        choices=[
            ("PCI Express 3.0", "PCI Express 3.0"),
            ("PCI Express 4.0", "PCI Express 4.0"),
            ("PCI Express 5.0", "PCI Express 5.0"),
        ],
        blank=True,
        null=True,
        help_text="Memory interface",
    )
    core_type = models.CharField(
        max_length=50,
        choices=[
            ("CUDA Cores", "CUDA Cores"),
            ("Stream Processors", "Stream Processors"),
            ("RDNA Cores", "RDNA Cores"),
            ("Xe Cores", "Xe Cores"),
        ],
        blank=True,
        null=True,
        help_text="Type of GPU cores",
    )
    dp_ports = models.CharField(
        max_length=50,
        choices=[
            ("DisplayPort x1", "DisplayPort x1"),
            ("DisplayPort x2", "DisplayPort x2"),
            ("DisplayPort x3", "DisplayPort x3"),
            ("DisplayPort x4", "DisplayPort x4"),
        ],
        blank=True,
        null=True,
        help_text="DisplayPort ports",
    )
    hdmi_ports = models.CharField(
        max_length=50,
        choices=[
            ("HDMI x1", "HDMI x1"),
            ("HDMI x2", "HDMI x2"),
            ("HDMI x3", "HDMI x3"),
            ("HDMI x4", "HDMI x4"),
        ],
        blank=True,
        null=True,
        help_text="HDMI ports",
    )
    vga_ports = models.CharField(
        max_length=50,
        choices=[
            ("VGA x1", "VGA x1"),
            ("VGA x2", "VGA x2"),
            ("VGA x3", "VGA x3"),
            ("VGA x4", "VGA x4"),
        ],
        blank=True,
        null=True,
        help_text="VGA ports",
    )
    dvi_ports = models.CharField(
        max_length=50,
        choices=[
            ("DVI x1", "DVI x1"),
            ("DVI x2", "DVI x2"),
            ("DVI x3", "DVI x3"),
            ("DVI x4", "DVI x4"),
        ],
        blank=True,
        null=True,
        help_text="DVI ports",
    )
    connectors = models.CharField(
        max_length=50,
        choices=[
            ("6 Pin Connector", "6 Pin Connector"),
            ("8 Pin Connector", "8 Pin Connector"),
            ("8+8 Pin Connector", "8+8 Pin Connector"),
            ("16 Pin Connector", "16 Pin Connector"),
        ],
        blank=True,
        null=True,
        help_text="Power connectors",
    )

    class Meta:
        verbose_name = "GPU"
        verbose_name_plural = "GPUs"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.vram_capacity})"


class PowerSupply(BaseProduct):
    image1 = models.ImageField(
        upload_to="psu_images/",
        blank=True,
        null=True,
        help_text="Image of the PSU (main)",
    )
    image2 = models.ImageField(
        upload_to="psu_images/",
        blank=True,
        null=True,
        help_text="Image of the PSU (optional)",
    )
    image3 = models.ImageField(
        upload_to="psu_images/",
        blank=True,
        null=True,
        help_text="Image of the PSU (optional)",
    )
    image4 = models.ImageField(
        upload_to="psu_images/",
        blank=True,
        null=True,
        help_text="Image of the PSU (optional)",
    )
    image5 = models.ImageField(
        upload_to="psu_images/",
        blank=True,
        null=True,
        help_text="Image of the PSU (optional)",
    )
    form_factor = models.CharField(
        max_length=50,
        choices=[
            ("ATX", "ATX"),
            ("SFX", "SFX"),
        ],
        blank=True,
        null=True,
        help_text="Form factor",
    )
    wattage = models.IntegerField(
        blank=True,
        null=True,
        help_text="Wattage",
    )
    efficiency = models.CharField(
        max_length=50,
        choices=[
            ("80 Plus", "80 Plus"),
            ("80 Plus White", "80 Plus White"),
            ("80 Plus Bronze", "80 Plus Bronze"),
            ("80 Plus Silver", "80 Plus Silver"),
            ("80 Plus Gold", "80 Plus Gold"),
            ("80 Plus Platinum", "80 Plus Platinum"),
            ("80 Plus Titanium", "80 Plus Titanium"),
        ],
        blank=True,
        null=True,
        help_text="Efficiency rating",
    )
    modularity = models.CharField(
        max_length=50,
        choices=[
            ("Non-Modular", "Non-Modular"),
            ("Semi-Modular", "Semi-Modular"),
            ("Fully Modular", "Fully Modular"),
        ],
        blank=True,
        null=True,
        help_text="Modularity",
    )
    fan_size = models.CharField(
        max_length=50,
        choices=[
            ("80 mm", "80 mm"),
            ("92 mm", "92 mm"),
            ("120 mm", "120 mm"),
            ("140 mm", "140 mm"),
            ("200 mm", "200 mm"),
        ],
        blank=True,
        null=True,
        help_text="Fan size",
    )

    class Meta:
        verbose_name = "Power Supply"
        verbose_name_plural = "Power Supplies"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.wattage}W)"


class Casing(BaseProduct):
    image1 = models.ImageField(
        upload_to="casing_images/",
        blank=True,
        null=True,
        help_text="Image of the Casing (main)",
    )
    image2 = models.ImageField(
        upload_to="casing_images/",
        blank=True,
        null=True,
        help_text="Image of the Casing (optional)",
    )
    image3 = models.ImageField(
        upload_to="casing_images/",
        blank=True,
        null=True,
        help_text="Image of the Casing (optional)",
    )
    image4 = models.ImageField(
        upload_to="casing_images/",
        blank=True,
        null=True,
        help_text="Image of the Casing (optional)",
    )
    image5 = models.ImageField(
        upload_to="casing_images/",
        blank=True,
        null=True,
        help_text="Image of the Casing (optional)",
    )
    type = models.CharField(
        max_length=50,
        choices=[
            ("Full Tower", "Full Tower"),
            ("Mid Tower", "Mid Tower"),
            ("Mini Tower", "Mini Tower"),
            ("Micro Tower", "Micro Tower"),
            ("Ultra Slim", "Ultra Slim"),
        ],
        blank=True,
        null=True,
        help_text="Type of case",
    )
    form_factor = models.CharField(
        max_length=50,
        choices=[
            ("ATX", "ATX"),
            ("Micro-ATX", "Micro-ATX"),
            ("Mini-ITX", "Mini-ITX"),
            ("E-ATX", "E-ATX"),
        ],
        blank=True,
        null=True,
        help_text="Form factor",
    )
    side_panel = models.CharField(
        max_length=50,
        choices=[
            ("Tempered Glass", "Tempered Glass"),
            ("Solid", "Solid"),
            ("Plastic", "Plastic"),
            ("Mesh", "Mesh"),
        ],
        blank=True,
        null=True,
        help_text="Side panel",
    )
    ssd_bays = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of SSD bays",
    )
    hdd_bays = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of HDD bays",
    )
    expansion_slots = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of expansion slots",
    )
    fan_support = models.CharField(
        max_length=50,
        choices=[
            ("80 mm", "80 mm"),
            ("92 mm", "92 mm"),
            ("120 mm", "120 mm"),
            ("140 mm", "140 mm"),
            ("200 mm", "200 mm"),
        ],
        blank=True,
        null=True,
        help_text="Fan support",
    )
    radiator_support = models.CharField(
        max_length=50,
        choices=[
            ("120 mm", "120 mm"),
            ("140 mm", "140 mm"),
            ("240 mm", "240 mm"),
            ("280 mm", "280 mm"),
            ("360 mm", "360 mm"),
            ("420 mm", "420 mm"),
            ("480 mm", "480 mm"),
        ],
        blank=True,
        null=True,
        help_text="Radiator support",
    )
    rgb = models.BooleanField(
        blank=True,
        null=True,
        help_text="RGB lighting",
    )
    dust_filters = models.BooleanField(
        blank=True,
        null=True,
        help_text="Dust filters",
    )
    cable_management = models.BooleanField(
        blank=True,
        null=True,
        help_text="Cable management",
    )
    power_supply = models.BooleanField(
        blank=True,
        null=True,
        help_text="With power supply",
    )
    pre_installed_fans = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of pre-installed fans",
    )

    class Meta:
        verbose_name = "Casing"
        verbose_name_plural = "Casings"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.form_factor})"


"""
Accessories:
1. Monitor
2. Keyboard
3. Mouse
4. Headphone
"""


class Monitor(BaseProduct):
    image1 = models.ImageField(
        upload_to="monitor_images/",
        blank=True,
        null=True,
        help_text="Image of the Monitor (main)",
    )
    image2 = models.ImageField(
        upload_to="monitor_images/",
        blank=True,
        null=True,
        help_text="Image of the Monitor (optional)",
    )
    image3 = models.ImageField(
        upload_to="monitor_images/",
        blank=True,
        null=True,
        help_text="Image of the Monitor (optional)",
    )
    image4 = models.ImageField(
        upload_to="monitor_images/",
        blank=True,
        null=True,
        help_text="Image of the Monitor (optional)",
    )
    image5 = models.ImageField(
        upload_to="monitor_images/",
        blank=True,
        null=True,
        help_text="Image of the Monitor (optional)",
    )
    screen_resolution = models.CharField(
        max_length=25,
        choices=[
            ("1280 x 720", "1280 x 720"),
            ("1920 x 1080", "1920 x 1080"),
            ("2560 x 1440", "2560 x 1440"),
            ("3840 x 2160", "3840 x 2160"),
            ("7680 x 4320", "7680 x 4320"),
            ("2560 x 1080", "2560 x 1080"),
            ("3440 x 1440", "3440 x 1440"),
            ("5120 x 2160", "5120 x 2160"),
            ("5120 x 1440", "5120 x 1440"),
        ],
        blank=True,
        null=True,
        help_text="Screen Resolution",
    )
    aspect_ratio = models.CharField(
        max_length=25,
        choices=[
            ("16:9", "16:9"),
            ("21:9", "21:9"),
            ("32:9", "32:9"),
        ],
        blank=True,
        null=True,
        help_text="Aspect Ratio",
    )
    screen_size = models.CharField(
        max_length=50,
        choices=[
            ("18-inch", "18-inch"),
            ("22-inch", "22-inch"),
            ("24-inch", "24-inch"),
            ("32-inch", "32-inch"),
            ("29-inch", "29-inch"),
            ("34-inch", "34-inch"),
            ("38-inch", "38-inch"),
        ],
        blank=True,
        null=True,
        help_text="Screen Size",
    )
    vga_ports = models.CharField(
        max_length=50,
        choices=[
            ("VGA x1", "VGA x1"),
            ("VGA x2", "VGA x2"),
            ("VGA x3", "VGA x3"),
            ("VGA x4", "VGA x4"),
        ],
        blank=True,
        null=True,
        help_text="VGA ports",
    )
    hdmi_ports = models.CharField(
        max_length=50,
        choices=[
            ("HDMI x1", "HDMI x1"),
            ("HDMI x2", "HDMI x2"),
            ("HDMI x3", "HDMI x3"),
            ("HDMI x4", "HDMI x4"),
        ],
        blank=True,
        null=True,
        help_text="HDMI ports",
    )
    dp_ports = models.CharField(
        max_length=50,
        choices=[
            ("DisplayPort x1", "DisplayPort x1"),
            ("DisplayPort x2", "DisplayPort x2"),
            ("DisplayPort x3", "DisplayPort x3"),
            ("DisplayPort x4", "DisplayPort x4"),
        ],
        blank=True,
        null=True,
        help_text="DisplayPort ports",
    )
    dvi_ports = models.CharField(
        max_length=50,
        choices=[
            ("DVI x1", "DVI x1"),
            ("DVI x2", "DVI x2"),
            ("DVI x3", "DVI x3"),
            ("DVI x4", "DVI x4"),
        ],
        blank=True,
        null=True,
        help_text="DVI ports",
    )
    usb_c_ports = models.CharField(
        max_length=50,
        choices=[
            ("USB-C x1", "USB-C x1"),
            ("USB-C x2", "USB-C x2"),
            ("USB-C x3", "USB-C x3"),
            ("USB-C x4", "USB-C x4"),
        ],
        blank=True,
        null=True,
        help_text="USB-C ports",
    )
    usb_ports = models.CharField(
        max_length=50,
        choices=[
            ("USB x1", "USB x1"),
            ("USB x2", "USB x2"),
            ("USB x3", "USB x3"),
            ("USB x4", "USB x4"),
        ],
        blank=True,
        null=True,
        help_text="USB ports",
    )
    speakers = models.BooleanField(
        blank=True,
        null=True,
        help_text="Built-in speakers",
    )
    refresh_rate = models.IntegerField(
        blank=True,
        null=True,
        help_text="Refresh rate in Hz",
    )
    response_time = models.IntegerField(
        blank=True,
        null=True,
        help_text="Response time in ms",
    )
    brightness = models.IntegerField(
        blank=True,
        null=True,
        help_text="Brightness in cd/m²",
    )

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitors"

    def __str__(self):
        return f"{self.brand} {self.model} {self.screen_size} {self.screen_resolution}"


class Keyboard(BaseProduct):
    image1 = models.ImageField(
        upload_to="keyboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Keyboard (main)",
    )
    image2 = models.ImageField(
        upload_to="keyboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Keyboard (optional)",
    )
    image3 = models.ImageField(
        upload_to="keyboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Keyboard (optional)",
    )
    image4 = models.ImageField(
        upload_to="keyboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Keyboard (optional)",
    )
    image5 = models.ImageField(
        upload_to="keyboard_images/",
        blank=True,
        null=True,
        help_text="Image of the Keyboard (optional)",
    )
    key_type = models.CharField(
        max_length=20,
        choices=[
            ("Membrane", "Membrane"),
            ("Mechanical", "Mechanical"),
        ],
        blank=True,
        null=True,
        help_text="Key Types",
    )
    interface = models.CharField(
        max_length=50,
        choices=[
            ("USB-A", "USB-A"),
            ("PS-2", "PS-2"),
            ("Wireless", "Wireless"),
            ("USB Type-C", "USB Type-C"),
        ],
        blank=True,
        null=True,
        help_text="Interface",
    )
    keyboard_size = models.CharField(
        max_length=50,
        choices=[
            ("Full-size Keyboard (100%)", "Full-size Keyboard (100%)"),
            ("Tenkeyless Keyboard (TKL) (~87%)", "Tenkeyless Keyboard (TKL) (~87%)"),
            ("75% Keyboard (~75%)", "75% Keyboard (~75%)"),
            ("65% Keyboard (~65%)", "65% Keyboard (~65%)"),
            ("60% Keyboard (~60%)", "60% Keyboard (~60%)"),
        ],
        blank=True,
        null=True,
        help_text="Keyboard Size",
    )
    number_of_keys = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of keys",
    )
    switch_type = models.CharField(
        max_length=50,
        choices=[
            ("Standard", "Standard"),
            ("Blue", "Blue"),
            ("Red", "Red"),
            ("Brown", "Brown"),
            ("Yellow", "Yellow"),
            ("Green", "Green"),
            ("Silver", "Silver"),
            ("Silent", "Silent"),
            ("Tactile", "Tactile"),
            ("Clicky", "Clicky"),
            ("Linear", "Linear"),
            ("Speed", "Speed"),
            ("Optical", "Optical"),
        ],
        blank=True,
        null=True,
        help_text="Switch Type",
    )
    cable_length = models.IntegerField(
        blank=True,
        null=True,
        help_text="Cable length in meters",
    )
    rgb = models.BooleanField(
        blank=True,
        null=True,
        help_text="RGB lighting",
    )

    class Meta:
        verbose_name = "Keyboard"
        verbose_name_plural = "Keyboards"

    def __str__(self):
        return f"{self.model} {self.brand} ({self.key_type})"


class Mouse(BaseProduct):
    image1 = models.ImageField(
        upload_to="mouse_images/",
        blank=True,
        null=True,
        help_text="Image of the Mouse (main)",
    )
    image2 = models.ImageField(
        upload_to="mouse_images/",
        blank=True,
        null=True,
        help_text="Image of the Mouse (optional)",
    )
    image3 = models.ImageField(
        upload_to="mouse_images/",
        blank=True,
        null=True,
        help_text="Image of the Mouse (optional)",
    )
    image4 = models.ImageField(
        upload_to="mouse_images/",
        blank=True,
        null=True,
        help_text="Image of the Mouse (optional)",
    )
    image5 = models.ImageField(
        upload_to="mouse_images/",
        blank=True,
        null=True,
        help_text="Image of the Mouse (optional)",
    )
    mouse_type = models.CharField(
        max_length=20,
        choices=[
            ("Membrane", "Membrane"),
            ("Mechanical", "Mechanical"),
        ],
        blank=True,
        null=True,
        help_text="Mouse Types",
    )
    interface = models.CharField(
        max_length=50,
        choices=[
            ("USB-A", "USB-A"),
            ("PS-2", "PS-2"),
            ("Wireless", "Wireless"),
            ("USB Type-C", "USB Type-C"),
        ],
        blank=True,
        null=True,
        help_text="Interface",
    )
    use_type = models.CharField(
        max_length=50,
        choices=[
            ("Gaming", "Gaming"),
            ("Office", "Office"),
        ],
        blank=True,
        null=True,
        help_text="Mouse Type",
    )
    number_of_buttons = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of buttons",
    )
    max_dpi = models.IntegerField(
        blank=True,
        null=True,
    )
    cable_length = models.IntegerField(
        blank=True,
        null=True,
    )
    rgb = models.BooleanField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Mouse"
        verbose_name_plural = "Mice"

    def __str__(self):
        return f"{self.brand} {self.model} {self.rgb} {self.use_type}"


class Headphone(BaseProduct):
    image1 = models.ImageField(
        upload_to="headphone_images/",
        blank=True,
        null=True,
        help_text="Image of the Headphone (main)",
    )
    image2 = models.ImageField(
        upload_to="headphone_images/",
        blank=True,
        null=True,
        help_text="Image of the Headphone (optional)",
    )
    image3 = models.ImageField(
        upload_to="headphone_images/",
        blank=True,
        null=True,
        help_text="Image of the Headphone (optional)",
    )
    image4 = models.ImageField(
        upload_to="headphone_images/",
        blank=True,
        null=True,
        help_text="Image of the Headphone (optional)",
    )
    image5 = models.ImageField(
        upload_to="headphone_images/",
        blank=True,
        null=True,
        help_text="Image of the Headphone (optional)",
    )
    headphone_type = models.CharField(
        max_length=50,
        choices=[
            ("Standard", "Standard"),
            ("Gaming", "Gaming"),
            ("Studio", "Studio"),
            ("Professional", "Professional"),
        ],
        blank=True,
        null=True,
        help_text="Headphone Type",
    )
    connection = models.CharField(
        max_length=50,
        choices=[
            ("Wired", "Wired"),
            ("Wireless", "Wireless"),
        ],
        blank=True,
        null=True,
        help_text="Connection",
    )
    microphone = models.BooleanField(
        blank=True,
        null=True,
        help_text="Microphone",
    )
    noise_cancellation = models.BooleanField(
        blank=True,
        null=True,
        help_text="Noise Cancellation",
    )
    rgb = models.BooleanField(
        blank=True,
        null=True,
        help_text="RGB lighting",
    )
    frequency_response = models.CharField(
        max_length=50,
        choices=[
            ("20 Hz - 20 kHz", "20 Hz - 20 kHz"),
            ("10 Hz - 40 kHz", "10 Hz - 40 kHz"),
            ("5 Hz - 50 kHz", "5 Hz - 50 kHz"),
        ],
        blank=True,
        null=True,
        help_text="Frequency Response",
    )
    impedance = models.IntegerField(
        blank=True,
        null=True,
        help_text="Impedance in ohms",
    )
    sensitivity = models.IntegerField(
        blank=True,
        null=True,
        help_text="Sensitivity in dB",
    )
    input_jack = models.CharField(
        max_length=50,
        choices=[
            ("3.5 mm", "3.5 mm"),
            ("USB-A", "USB-A"),
            ("USB-C", "USB-C"),
        ],
        blank=True,
        null=True,
        help_text="Input Jack",
    )
    cable_length = models.IntegerField(
        blank=True,
        null=True,
        help_text="Cable length in meters",
    )

    class Meta:
        verbose_name = "Headphone"
        verbose_name_plural = "Headphones"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.headphone_type})"
