import pytest
class NegativeValueError(Exception):
    """Bill and percentage are negative"""
    pass


# function que j'ai envie d'implementer

def total_with_tip(bill, percentage):
    if bill <0 :
        raise NegativeValueError("Bill should be positive")
    if percentage <0 :
        raise NegativeValueError("Percentage should be positive")
    
    tip = bill* percentage/100
    if tip>500:
        tip = 500
    total = bill + tip
    if total<5:
        total = 5
    return round(total,2)




# TTD - test driven development
# 1. Pour un repas à *100€* (bill), et un tips de *20%*(percentage) : Je laisse sur la table *120€*

def test_tip_classic():
    assert total_with_tip(100, 20) == 120

def test_tip_poor_service():
    assert total_with_tip(100, 0) == 100

def test_tip_max():
    assert total_with_tip(1000,51) == 1500
    assert total_with_tip(5000,15) == 5500
    assert total_with_tip(2000,26)== 2500
    assert total_with_tip(10000,12) == 10500

def test_total_min():
    assert total_with_tip(1,0) == 5
    assert total_with_tip(2.3,20) == 5
    assert total_with_tip(4,15) == 5
    assert total_with_tip(3,50) == 5

def test_two_decimals():
    assert total_with_tip(10.12,15) == 11.64
    assert total_with_tip(10,2.33) == 10.23 

def test_negative_error():
    with pytest.raises(NegativeValueError) as exceptionTips:
        total_with_tip(100,-10)
    assert str(exceptionTips.value) == "Percentage should be positive"

    with pytest.raises(NegativeValueError) as exceptionBill:
        total_with_tip(-10,10)
    assert str(exceptionBill.value) == "Bill should be positive"