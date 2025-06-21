from pydantic import BaseModel,Field,computed_field,field_validator,constr
from typing import Annotated,Literal
lowestr = Annotated[constr(to_lower=True), Field(...)]

class UserInput(BaseModel):
    marriage:Annotated[lowestr,Field(...,description='Marriage Status of Customer')]
    sex:Annotated[lowestr,Field(...,description="Gender of Customer")]
    education:Annotated[lowestr,Field(description='Education of the customer')]
    LIMIT_BAL:Annotated[float,Field(description='Credit Limit Assigned to Customer')]
    pay_0:Annotated[Literal[-2,-1,0,1,2,3,4,5,6,7,8],Field(description="""Payment status of customer in current month for the bill generated in previous month. -2 = No credit consumption (no bill) in month m−1 ●  -1 = Bill generated and fully paid in month m−1 (same month payment) ●  0= Partial or minimum payment made (revolving credit) ●  ≥1 = Payment delayed by that many months (1 = 1 month overdue, etc.) """)]
    pay_2:Annotated[Literal[-2,-1,0,1,2,3,4,5,6,7,8],Field(description="Payment status of customer 2 month ago for the bill generated in previous month.")]
    pay_3:Annotated[Literal[-2,-1,0,1,2,3,4,5,6,7,8],Field(description="Payment status of customer 3 month ago for the bill generated in previous month.")]
    pay_4:Annotated[Literal[-2,-1,0,1,2,3,4,5,6,7,8],Field(description="Payment status of customer 4 month ago for the bill generated in previous month.")]
    pay_5:Annotated[Literal[-2,-1,0,1,2,3,4,5,6,7,8],Field(description="Payment status of customer 5 month ago for the bill generated in previous month.")]
    pay_6:Annotated[Literal[-2,-1,0,1,2,3,4,5,6,7,8],Field(description="Payment status of customer 6 month ago for the bill generated in previous month.")]
    Bill_amt_1:Annotated[float,Field(description="Total bill at the end of last month")]
    Bill_amt_2:Annotated[float,Field(description="Total bill 2 month ago")]
    Bill_amt_3:Annotated[float,Field(description="Total bill 3 month ago")]
    Bill_amt_4:Annotated[float,Field(description="Total bill 4 month ago")]
    Bill_amt_5:Annotated[float,Field(description="Total bill 5 month ago")]
    Bill_amt_6:Annotated[float,Field(description="Total bill 6 month ago")]
    pay_amt1:Annotated[float,Field(description="Amount the customer paid last month, which was used to pay off the bill from 2 months ago")]
    pay_amt2:Annotated[float,Field(description="Amount paid 2 months ago, toward bill from 3 months ago")]
    pay_amt3:Annotated[float,Field(description="Amount paid 3 months ago, toward bill from 4 months ago")]
    pay_amt4:Annotated[float,Field(description="Amount paid 4 months ago, toward bill from 5 months ago")]
    pay_amt5:Annotated[float,Field(description="Amount paid 5 months ago, toward bill from 6 months ago")]
    pay_amt6:Annotated[float,Field(description="Amount paid 6 months ago, toward bill from 7 months ago")]
    @field_validator('marriage')
    @classmethod
    def normalize_marriage(cls,v:str)->str:
        if v not in {'single', 'married', 'others'}:
            raise ValueError("Marriage must be 'single', 'married', or 'others'")
        return v
    @field_validator('sex')
    @classmethod
    def normalize_sex(cls,v:str)->str:
        if v not in {'male', 'female'}:
            raise ValueError("Sex must be 'male' or 'female'")
        return v
    @field_validator('education')
    @classmethod
    def normalize_edu(cls,v:str)->str:
        if v not in {'university', 'high school', 'graduate school', 'others'}:
            raise ValueError("Education must be one of 'university', 'high school', 'graduate school', or 'others'")
        return v

    @computed_field
    @property
    def AVG_Bill_amt(self)->float:
        return (self.Bill_amt_1+self.Bill_amt_2+self.Bill_amt_3+self.Bill_amt_4+self.Bill_amt_5+self.Bill_amt_6)/6
    @computed_field
    @property
    def avg_pay_amt(self)->float:
        return (self.pay_amt1+self.pay_amt2+self.pay_amt3+self.pay_amt4+self.pay_amt5+self.pay_amt6)/6
    @computed_field
    @property
    def PAY_TO_BILL_ratio(self)->float:
        if self.AVG_Bill_amt==0:
            raise ZeroDivisionError
        return (self.avg_pay_amt)/(self.AVG_Bill_amt)
    @computed_field
    @property
    def utilization_ratio(self)->float:
        if self.LIMIT_BAL==0:
            raise ZeroDivisionError
        return (self.AVG_Bill_amt)/(self.LIMIT_BAL)
    @computed_field
    @property
    def delay_count(self)->int:
        
        return sum(1 for i in [self.pay_0, self.pay_2, self.pay_3, self.pay_4, self.pay_5, self.pay_6] if i > 1)
    @computed_field
    @property
    def marriage_status(self)->int:
        if self.marriage=='single':
            return 2
        elif self.marriage=='married':
            return 1
        else:
            return 3
        
    @computed_field
    @property
    def gender(self)->int:
        if self.sex=='male':
            return 1
        else:
            return 0

    @computed_field
    @property
    def edu_status(self)->int:
        if self.education=='university':
            return 2
        elif self.education=='graduate school':
            return 1
        elif self.education=='high school':
            return 3
        else:
            return 4        

    
