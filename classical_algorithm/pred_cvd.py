import random

dummy_data = [['봄', 30, 0, 160, 50, 3, 1, 1, 2, 2, 1.5], ['여름', 40, 0, 163, 53, 5, 2, 2, 4, 4, 2], ['가을', 25, 1, 180, 80, 3, 4, 4, 5, 5, 2], ['겨율', 35, 175, 67, 10, 5, 5, 6, 6, 2]]

def choose():
    i = random.randint(0, 3)
    return dummy_data[i]


def pred_cvd(data):
    name = data[0]
    age = data[1]
    sex = data[2]
    height = data[3]
    weight = data[4]
    body_fat_m = data[5]
    right_arm_m = data[6]
    left_arm_m = data[7]
    right_leg_m = data[8]
    left_leg_m = data[9]
    abfat = data[10]

    bfmi = body_fat_m / (height * height * 0.0001)
    lbmi = (weight - body_fat_m) / (height * height * 0.0001)
    asmi = (right_arm_m + left_arm_m + right_leg_m + left_leg_m) / (height * height * 0.0001)


    score = 0
    if sex == 0:
        if age >=14 and age <= 17:
            score = (lbmi - 0.735 * weight / height / height) - (bfmi - 0.265 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.38 / height / height) - (abfat - body_fat_m * 0.265 / height / height)
        elif age >= 18 and age <= 39:
            score = (lbmi - 0.725 * weight / height / height) - (bfmi - 0.275 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.36 / height / height) - (abfat - body_fat_m * 0.28 / height / height)
        elif age >= 40 and age <= 59:
            score = (lbmi - 0.71 * weight / height / height) - (bfmi - 0.29 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.34 / height / height) - (abfat - body_fat_m * 0.29 / height / height)
        else:
            score = (lbmi - 0.705 * weight / height / height) - (bfmi - 0.295 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.32 / height / height) - (abfat - body_fat_m * 0.41 / height / height)
    elif sex == 1:
        if age >=15 and age <= 17:
            score = (lbmi - 0.84 * weight / height / height) - (bfmi - 0.16 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.5 / height / height) - (abfat - body_fat_m * 0.135 / height / height)
        elif age >= 18 and age <= 39:
            score = (lbmi - 0.84 * weight / height / height) - (bfmi - 0.16 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.47 / height / height) - (abfat - body_fat_m * 0.155 / height / height)
        elif age >= 40 and age <= 59:
            score = (lbmi - 0.83 * weight / height / height) - (bfmi - 0.17 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.45 / height / height) - (abfat - body_fat_m * 0.165 / height / height)
        else:
            score = (lbmi - 0.8 * weight / height / height) - (bfmi - 0.2 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.41 / height / height) - (abfat - body_fat_m * 0.18 / height / height)
    score = score / 250
    return score

print(pred_cvd(choose()))