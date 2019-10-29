"""
Inventory Mgmt System : To add products, quantity & keep track of the products
"""


class Product():
    """
    Adding new product & its description
    """

    def __init__(self, prod_name, prod_desc):
        self.name = prod_name
        self.description = prod_desc

    def __repr__(self):
        """
        Shows product name & description of given product
        """
        return f"{self.name} - {self.description}"


class Warehouse():
    """
    Adding new warehouse, its location, and products they store inside the warehouse
    """

    def __init__(self, wh_location):
        self.location = wh_location
        self.list_of_products = []

    def add_product(self, new_prod):
        """
        Add new product to the selected warehouse
        """
        self.list_of_products.append(new_prod)

    def remove_product(self, delete_prod):
        """
        Remove new product to the selected warehouse
        """
        self.list_of_products.remove(delete_prod)

    def __repr__(self):
        return f"{self.location}"


# shows the store & warehouses located | add new warehouse & check product availability to that selected warehouse
class Store():
    """
    Adding the new stores & the list of warehouses under the store
    """

    def __init__(self, store_name):
        self.name = store_name
        self.warehouses = []

    def add_warehouse(self, new_warehouse):
        """
        Add new warehouse under the selected store.
        """
        self.warehouses.append(new_warehouse)

    def check_product_availability(self, product_name):
        """
        Input product_name , Output the availability of product from that selected warehouse
        """

        # lookup for all warehouses, then lookup for all products in each warehouses
        for wh in camera_store.warehouses:
            for prod in wh.list_of_products:
                if prod.name == product_name:
                    return {'lookup product': prod, 'warehouse availability': wh}
                else:
                    return "this product is not available, make sure the spelling is correct"


# the store
camera_store = Store(store_name='ABC Camera store')


# 2 warehouses under this one store
abc_warehouse_1 = Warehouse(wh_location='Wangsa Maju')
abc_warehouse_2 = Warehouse(wh_location='Cyberjaya')

camera_store.add_warehouse(new_warehouse=abc_warehouse_1)
camera_store.add_warehouse(new_warehouse=abc_warehouse_2)


# enter details of new product
sony_hd_camera = Product(
    'Sony HD Camera', 'Can capture image as far as 1000km')


# add the new product in warehouse2
abc_warehouse_2.add_product(sony_hd_camera)


# test to run availability check
product_search_term = 'Sony HD Camera'
find_product = camera_store.check_product_availability(
    product_name=product_search_term)

print(find_product)

# show which warehouse is that product is available
print(find_product['lookup product'])
print(find_product['warehouse availability'])
print(" ")
print(
    f"{find_product['lookup product']} is available in our {find_product['warehouse availability']} branch")
