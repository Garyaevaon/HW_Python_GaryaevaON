from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S25", "89565665223"),
    Smartphone("Motorola", "Edge 50 Specs", "89525454422"),
    Smartphone("Asus Zenfone", "11 Compact Specs", "89563521424"),
    Smartphone("Google", "Pixel 9 Pro XL Specs", "89546541425"),
    Smartphone("Blackview", "BV8900 Specs", "895627898426")
]

for smarphone in catalog:
    print(f"{smarphone.brand} - {smarphone.model}. {smarphone.number}.")