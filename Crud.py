
import ClothingBack
import ClosetBack
import DeviceBack
import FurnitureBack
import HomeApplianceBack
import ImportantItemBack
import MedicineBack
import PersonBack
import PetBack
import PetItemBack
import PetMedicineBack
import RoomBack
import SafeBack

"""
This is a function where all the processes of CRUD for all categories in the database are implemented.
"""


def crud(username, password):
    print("You can select which category you want to work on")
    print("Categories are:\nPerson, Device, Clothing, Medicine, Closet, Home appliances")
    print("Important item, Safe, Pet, Pet medicine, Pet item, Furniture, Room")
    print("Enter the name of the category you want to work on:")

    selected_category = input("Enter the category name as shown above: ")

    # 1 person
    if selected_category.lower() == "person":
        PersonBack.person(username, password)

    # 2 device
    elif selected_category.lower() == "device":
        DeviceBack.device(username, password)

    # 3 medicine
    elif selected_category.lower() == "medicine":
        MedicineBack.medicine(username, password)

    # 4 clothing
    elif selected_category.lower() == "clothing":
        ClothingBack.clothing(username, password)

    # 5 important item
    elif selected_category.lower() == "important item":
        ImportantItemBack.important(username, password)

    # 6 home appliance
    elif selected_category.lower() == "home appliances":
        HomeApplianceBack.home_appliance(username, password)

    # 7 pet medicine
    elif selected_category.lower() == "pet medicine":
        PetMedicineBack.pet_med(username, password)

    # 8 furniture
    elif selected_category.lower() == "furniture":
        FurnitureBack.furniture(username, password)

    # 9 safe
    elif selected_category.lower() == "safe":
        SafeBack.safe(username, password)

    # 10 pet
    elif selected_category.lower() == "pet":
        PetBack.pet(username, password)

    # 11 pet item
    elif selected_category.lower() == "pet item":
        PetItemBack.pet_item(username, password)

    # 12 room
    elif selected_category.lower() == "room":
        RoomBack.room(username, password)

    # 13 closet
    elif selected_category.lower() == "closet":
        ClosetBack.closet(username, password)

