# # Inbody data
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하시오: "))
sex = int(input("성별을 입력하시오(여자: 0, 남자: 1): "))
height = float(input("키를 입력하시오(cm): "))
weight = float(input("몸무게를 입력하시오(kg): "))
body_fat_m = float(input("체지방을 입력하시오(kg): "))
right_arm_m = float(input("오른팔 근육량을 입력하시오(kg): "))
left_arm_m = float(input("왼팔 근육량을 입력하시오(kg): "))
right_leg_m = float(input("오른 다리 근육량을 입력하시오(kg): "))
left_leg_m = float(input("왼 다리 근육량을 입력하시오(kg): "))
abfat = float(input("복부지방: "))

bfmi = body_fat_m / (height * height * 0.0001)
lbmi = (weight - body_fat_m) / (height * height * 0.0001)
asmi = (right_arm_m + left_arm_m + right_leg_m + left_leg_m) / (height * height * 0.0001)
bmi = lbmi + asmi

l = [age, sex, bfmi, lbmi, asmi, abfat]


score = 0


if sex == 1:
    if age >=15 and age <= 17:
        score = (lbmi - 0.84 * weight / height / height) - (bfmi - 0.16 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.5 / height / height) - (abfat - body_fat_m * 0.135 / height / height)
    elif age >= 18 and age <= 39:
        score = (lbmi - 0.84 * weight / height / height) - (bfmi - 0.16 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.47 / height / height) - (abfat - body_fat_m * 0.155 / height / height)
    elif age >= 40 and age <= 59:
        score = (lbmi - 0.83 * weight / height / height) - (bfmi - 0.17 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.45 / height / height) - (abfat - body_fat_m * 0.165 / height / height)
    else:
        score = (lbmi - 0.8 * weight / height / height) - (bfmi - 0.2 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.41 / height / height) - (abfat - body_fat_m * 0.18 / height / height)
elif sex == 0:
    if age >=14 and age <= 17:
        score = (lbmi - 0.735 * weight / height / height) - (bfmi - 0.265 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.38 / height / height) - (abfat - body_fat_m * 0.265 / height / height)
    elif age >= 18 and age <= 39:
        score = (lbmi - 0.725 * weight / height / height) - (bfmi - 0.275 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.36 / height / height) - (abfat - body_fat_m * 0.28 / height / height)
    elif age >= 40 and age <= 59:
        score = (lbmi - 0.71 * weight / height / height) - (bfmi - 0.29 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.34 / height / height) - (abfat - body_fat_m * 0.29 / height / height)
    else:
        score = (lbmi - 0.705 * weight / height / height) - (bfmi - 0.295 * weight / height / height) + 1.5 * (asmi - (weight - body_fat_m) * 0.32 / height / height) - (abfat - body_fat_m * 0.41 / height / height)

print(score / 100)