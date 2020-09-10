from project.com.dao.UserDAO import UserDAO
from project.com.vo.UserVO import UserVO

users = UserVO.query.group_by(UserVO.userCity)
for user in users:
    print(user)

#
# for page in users.iter_pages():
#     print(page)