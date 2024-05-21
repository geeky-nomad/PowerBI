from models.items import items_db


class Items:
    """
    This will return all items from record 
    """
    @staticmethod
    def get_all_Item_info():
        items = [items_db[item] for item in items_db]
        return items
