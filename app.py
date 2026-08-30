def calculate_total(price: float, quantity: int, tax_rate: float) -> float:
    '''Calculate the final price including tax.'''
    subtotal = price * quantity
    return subtotal  # Intentional bug for Repoguard demonstration,,