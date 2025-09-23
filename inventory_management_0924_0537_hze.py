# 代码生成时间: 2025-09-24 05:37:59
from django.db import models
def generate_random_number():
    """Generates a random number for inventory item ID."""
    import random
    return random.randint(1000, 9999)

class Item(models.Model):
    """Model representing an item in inventory."""
    id = models.IntegerField(primary_key=True, default=generate_random_number)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """String representation of the Item."""
        return self.name

    class Meta:
        """Meta options for the Item model."""
        verbose_name_plural = 'Items'

class InventoryManager(models.Manager):
    """Custom manager for inventory operations."""
    def add_item(self, item_name, quantity, description=""):
        """Adds a new item to the inventory."""
        item, created = Item.objects.get_or_create(name=item_name)
        if created:
            item.quantity = quantity
            item.description = description
            item.save()
            return True, "Item added successfully."
        else:
            return False, "Item already exists in inventory."

    def update_item(self, item_name, new_quantity):
        """Updates the quantity of an item in the inventory."""
        try:
            item = Item.objects.get(name=item_name)
            if new_quantity < 0:
                return False, "Quantity cannot be negative."
            item.quantity = new_quantity
            item.save()
            return True, "Item updated successfully."
        except Item.DoesNotExist:
            return False, "Item not found in inventory."

    def remove_item(self, item_name):
        """Removes an item from the inventory."""
        try:
            item = Item.objects.get(name=item_name)
            item.delete()
            return True, "Item removed successfully."
        except Item.DoesNotExist:
            return False, "Item not found in inventory."

class Inventory(models.Model):
    """Model representing an inventory."""
    items = InventoryManager()

    def __str__(self):
        """String representation of the Inventory."""
        return "Inventory"

    class Meta:
        """Meta options for the Inventory model."""
        verbose_name_plural = 'Inventories'

# Example usage:
# inventory = Inventory()
# success, message = inventory.items.add_item("Widget", 50)
# print(message)
