import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="abcdef", key="!")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=12312312, key=2)

    encrypted_bondinho_even = encrypt_message("bondinho", 2)
    assert encrypted_bondinho_even == "ohnidn_ob"

    encrypted_bondinho_odd = encrypt_message("bondinho", 5)
    assert encrypted_bondinho_odd == "idnob_ohn"

    encrypted_bondinho_out_of_range = encrypt_message("bondinho", 10)
    assert encrypted_bondinho_out_of_range == "ohnidnob"
