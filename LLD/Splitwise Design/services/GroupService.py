class GroupService:
    def __init__(self, expenseService):
        self.expenseService = expenseService

    def getPaymentGraph(self, groupId, userId):
        if (userId not in User):
            return Exception('Illegal Access')
        groupExpense = self.expenseService.getGroupExpense(groupId)
        resultExpense = self.sumExpense(groupExpense)
        return self.expenseService.getGroupExpense(resultExpense)


    def sumExpense(self, groupExpense):
        return groupExpense