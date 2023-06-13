import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="abcdef", key="!")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=12312312, key=2)

    encryptedBondinhoEven = encrypt_message("bondinho", 2)
    assert encryptedBondinhoEven == "ohnidn_ob"

    encryptedBondinhoOdd = encrypt_message("bondinho", 5)
    assert encryptedBondinhoOdd == "idnob_ohn"

    encryptedBondinhoOdd = encrypt_message("bondinho", 10)
    assert encryptedBondinhoOdd == "ohnidnob"
