from pytest import MonkeyPatch

from entities.user_interaction import UserInteraction


def test_get_user_input(monkeypatch: MonkeyPatch):
    # Arrange
    user_interaction = UserInteraction()

    # Act
    monkeypatch.setattr("builtins.input", lambda _: "0")
    result0 = user_interaction.get_opcao_by_user()

    monkeypatch.setattr("builtins.input", lambda _: "1")
    result1 = user_interaction.get_opcao_by_user()

    monkeypatch.setattr("builtins.input", lambda _: "2")
    result2 = user_interaction.get_opcao_by_user()

    monkeypatch.setattr("builtins.input", lambda _: "3")
    result3 = user_interaction.get_opcao_by_user()

    monkeypatch.setattr("builtins.input", lambda _: "4")
    result4 = user_interaction.get_opcao_by_user()

    monkeypatch.setattr("builtins.input", lambda _: "5")
    result5 = user_interaction.get_opcao_by_user()

    monkeypatch.setattr("builtins.input", lambda _: "6")
    result6 = user_interaction.get_opcao_by_user()

    # Assert
    assert result0 == False
    assert result1 == True
    assert result2 == True
    assert result3 == True
    assert result4 == True
    assert result5 == True
    assert result6 == False
    assert type(result0) == bool
    assert type(result1) == bool
    assert type(result2) == bool
    assert type(result3) == bool
    assert type(result4) == bool
    assert type(result5) == bool
    assert type(result6) == bool
