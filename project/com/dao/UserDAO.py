from project.com.vo.UserVO import UserVO

class UserDAO:
    def viewUsers(self,page,per_page):
        results = UserVO.query.order_by(UserVO.userId.desc()).paginate(page=page,per_page=per_page)
        return results