from typing import Tuple
from random import randint


class RiskBattleSimulator:
    @staticmethod
    def _simulate_one_throw(attacker_dice_count: int, defender_dice_count: int) -> Tuple[int, int]:
        assert (0 <= attacker_dice_count <= 3 and 0 <= defender_dice_count <= 2)

        attacker_throw = sorted([randint(1, 6) for _ in range(attacker_dice_count)], reverse=True)
        defender_throw = sorted([randint(1, 6) for _ in range(defender_dice_count)], reverse=True)

        while len(attacker_throw) > 0 and len(defender_throw) > 0:
            if attacker_throw[0] > defender_throw[0]:
                defender_dice_count -= 1
            else:
                attacker_dice_count -= 1
            attacker_throw.pop(0)
            defender_throw.pop(0)

        return attacker_dice_count, defender_dice_count

    def bliz(self, attacker_dice_count: int, defender_dice_count: int) -> Tuple[int, int]:
        """Keep rolling the dice until either you've conquered the territory or are out."""
        assert (0 <= attacker_dice_count and 0 <= defender_dice_count)

        while attacker_dice_count > 1 and defender_dice_count > 0:
            attack_with = min(3, attacker_dice_count-1)
            defend_with = min(2, defender_dice_count)

            attack_res, defend_res = self._simulate_one_throw(attack_with, defend_with)

            attacker_dice_count -= attack_with - attack_res
            defender_dice_count -= defend_with - defend_res

        return attacker_dice_count, defender_dice_count


if __name__ == '__main__':
    attack_with = int(input("Attack with: "))
    defend_with = int(input("Defend with: "))

    attack_res, defend_res = RiskBattleSimulator().bliz(attack_with, defend_with)
    print("Battle Ended!")

    print(f"Remaining attacker tropes: {attack_res}")
    print(f"Remaining defender tropes: {defend_res}")
