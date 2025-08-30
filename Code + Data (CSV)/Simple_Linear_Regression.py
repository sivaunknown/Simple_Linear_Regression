import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Simple_Linear_Regression:

    def __init__(self):
        self.x : pd.DataFrame
        self.y : pd.DataFrame
        self.y_pred : list = []
        self.x_mean : float
        self.y_mean : float
        self.slope : float
        self.y_intercept : float

    def load_data(self,data_file : str) -> pd.DataFrame:
        dataframe : pd.DataFrame = pd.read_csv(data_file)
        x : pd.DataFrame = dataframe["YearsExperience"]
        y : pd.DataFrame = dataframe["Salary"]
        return x,y

    def find_means(self,x : pd.DataFrame,y : pd.DataFrame) -> list:
        x_mean : float = np.mean(x)
        y_mean : float = np.mean(y)
        return [x_mean,y_mean]

    def find_slope(self,x : pd.DataFrame,y : pd.DataFrame, x_mean : float, y_mean : float)-> float:
        numerator : float = np.sum((x-x_mean)*(y-y_mean))
        denominator : float = np.sum((x - x_mean)**2)
        return numerator/denominator
    
    def find_y_intercept(self,slope_m : float, x_mean : float, y_mean : float) -> float:
        return y_mean - slope_m*x_mean
    
    def pred_y(self,slope : float,x : pd.DataFrame, c : float) -> None:
        for x_i in x:
            self.y_pred.append(slope*x_i+c)

    def plot_pred_line(self,x : pd.DataFrame, y : pd.DataFrame, y_pred : list) -> None :
        plt.scatter(x,y)
        plt.xlabel("Years of Exp")
        plt.ylabel("Salary")
        plt.title("Exp vs Salary")
        plt.plot(x,y_pred,color='red')
        plt.show()
    
    def pred_single_value(self,x):
        self.get_params()
        predicted_y : float = (self.slope*x+self.y_intercept)
        print("The Predicted Salary for ",x, " years of exp : ",predicted_y)
        plt.scatter(self.x,self.y)
        plt.scatter(x,predicted_y,color = "green", marker="X")
        plt.axhline(y=predicted_y, linestyle='--', color='gray')  # Horizontal line
        plt.axvline(x=x, linestyle='--', color='gray')  # Vertical line
        plt.show()

    def r_squared(self,y_actual, y_pred) -> None:
        y_mean = np.mean(y_actual)
        ss_total = np.sum((y_actual - y_mean) ** 2)
        ss_residual = np.sum((y_actual - y_pred) ** 2)
        print ("Accuracy of the model : ",int(round(1 - (ss_residual / ss_total),2) * 100),"%")

    def get_params(self) -> None:
        self.x,self.y = self.load_data("Salary_dataset.csv")
        self.x_mean,self.y_mean = self.find_means(self.x,self.y)
        self.slope = self.find_slope(self.x,self.y,self.x_mean,self.y_mean)
        self.y_intercept = self.find_y_intercept(self.slope,self.x_mean,self.y_mean)

    def main(self) -> None:
        self.get_params()
        self.pred_y(self.slope,self.x,self.y_intercept)
        self.r_squared(self.y,self.y_pred)
        self.plot_pred_line(self.x,self.y,self.y_pred)


s = Simple_Linear_Regression()
s.main()
s.pred_single_value(7.0)




