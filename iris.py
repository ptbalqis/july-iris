import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

st.image('https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification.png')
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/ptbalqis/july-iris/main/IRIS.csv')
X = iris.drop('species', axis = 1)
Y = iris['species']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
dataf= pd.DataFrame(['Iris-setosa','Iris-versicolor','Iris-virginica'])
st.write(dataf) 

st.subheader('Prediction')
st.write(prediction)
if prediction=='Iris-setosa':
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0pMxs3Jy6ARLMqvfPBLD-BiMppNfc9eeQZg&usqp=CAU")
elif prediction=='Iris-versicolor':
    st.image("data:image/jpeg;base64,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")
elif prediction=='Iris-virginica':
    st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgWFRYYGBgaGBoYGhoaGBgaGhgaGBkZGRgYGBgcIS4lHB4rIRgYJjgmKy8xNTU2GiQ7QDszPy40NTQBDAwMEA8QHhISHzQrJSw0NDQ0NjQ0NDQ0NDQ0NDQ0NDQ1NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NP/AABEIAMIBBAMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAEBQMGAAIHAQj/xAA/EAABAwMCAwYDBgMHBAMAAAABAAIRAwQhEjEFQVEGImFxgZETMqFCUrHB0fBicuEHFBUjgpLxorLC0lNjc//EABoBAAMBAQEBAAAAAAAAAAAAAAIDBAEFAAb/xAArEQACAgEEAQQCAgEFAAAAAAAAAQIRAwQSITFBBRMiUWFxgbEyFDORofD/2gAMAwEAAhEDEQA/AOXq6dk7bEqp0qcuA8V0jgFrpYFztRPhIkyS4oZVWd1VzizHN7ys9w6Eu4jSD2EeCXGXyPYJ7ZWUpzy/AXophoWlVjmPIhR3FzAVbd9HTjtrcyO4utKV1bouKjruc8oulZkAYTElEXKW58D/ALD2eutJGAu12zAxnouZdiLUs7xETlXu54iAzSkSdybJ50mVXtdXLzoHMpZZWmgJjcN1v1FSMpqaU9zpE8sra2o0YxSEgLHvAQVe6DRJWKS6QoM1jcmB1SDjHaYMJYwS7Y9PIpNxvjrnAsbt1VeoNkyVbjjxZRDHSthdesXEuccnPkga1acKa4fAQbG5T4ofFG7HIhr1q1izSiCCKb1I8ghDMdC1fVQvk1M0qqJegyvHtWp0eCrBx1QFceG2ZMSFV+zbAakH0XTLSgA1SZ5fKibM+aA3s0tVe4jfaepTzjNfSMKlX91qJQ4+ZUBjVyF97XL3SUEd1I9ymoW5OVY2ooqbSQdwyz1bp3/hoa2YS3hlfSYTu8uhoXNyym514JZW5FZuaQ1FeKG4fLiVit2j9o04dbzUaF03htKGhI7CxY58gZVqtqUD0XKzze5CM0HGVMX8UMApJbXjTIcU542w6TC5rXrVGPO8SU7D8rMhGywX7GuMoahwzWdkFaXkkSrVwqszwTpScQnvXAIezrGiYyoGcJVgv7gYARNswBmUqU5JXZscsovgzhYa1gBxCX3dw9zzGy9uK5nSFCzV0S3kcuEKyZNzDbZmMravUhC/Ecgr+80jqeQQ3b2w7AVvhE1WsBuVX+LViQY2Xhe8mXED+Gc+sLSodbYBAPqulD03UpJ7SiOFrkrFcyVIzAU1xw97HQ5p5mRkEDnIQtd8BP2OPxaod+CGvUkrRr1DqytkQaCfioqnaPOTDR/Fv56d1twil3XVOeoNb4Y1OMerfqmOjadz/RXYNIpx3M0DfYsAMvcTiIaBHic5CHPDHH5XNcemx9DtKOqPlQGoRkKiWkx10bQExkYIgjBCk0o7Syrky10RqEEEjm4f1S97XNdpIz+PiPBc3NglDl9eGZyux92ZtJfqXQNbWN9FTOA0XgTCf1Ld7xC5c3cmyPLK5cG1VrXnqqzx/hkfKFabWwcxS1bQO3CmgpRybrFxbi7OY0+GPcRIVjo8OAbtyVnFgwclo+3Cpyzcw5ZHIpjuHkOkdVJVt3EQrQ+2CFqW4WKTXIKkyp/4eV6rEaIWI/ekF70j3slfPe4grolF+MrmvYYjUZ6rpNSn3Zaufqvjko9lbcuQHisBpVGuCxxO25Vj4/ewwg9FzZ1y4E55lP08W02MwzpPgbvYAcL2ldFpkFKP7yTzW1OoSVUl9jXJMstjxAueJVgqXJIEJL2fsA5uU7o0IJaVFlknLaibNKLdRNm6WjUUPdcTbsERcUhGmUmvLdrATKVa/wAUJ56I7niZCEpVy5hfGdRE+AjA6JY8l7sbJjZUSGFp5On3H9F2/SccI51fdFOFJMEe76/sKAPIKnrs3UYG3v8Akf1X1TLEYx7pG6ScXo6HwNiNQ8jy9FYGM3/fVA8atC5msfY3/lMAn0IH1UOsw7sd+VyYyuL2VhCxlJxOAuOCWngto51u0NElznuEDyYP+wmUeLB4kEHA6c8HHUQ76Jz2St9NKmCIcGA7DMuIjH/6T5geasFbh5c2WtnfriQQR4SCuvgnWNUZbOZXNIgyB/UxJjwS6oCVeL6xYGnBLtsg93MwJ8TvO+TyAqla2cN+vn/x/Rbvc1VNBxl4IbUREKy9m+HNrvfI+TTHk7V/6qvNbCufYRpa2q87OLWjx0aiT/1BJ9QajpWv0DlfxLFQ4c1giFPoaEDc8UaMSl1xxbovmURNocveAhalwFVrrjh6pTW42+eaOMWzyi2XWrdjqEDWvx1VRdxR5Uf+IHmtcGa4MstXiI6oZ/ER1VYq3TiUw4ZYveZOyZ7aStsP2UlbGnxCcrxNKVsAAFiTuQukLuxzJMjquhU7gtwdlzTgVz8N/qroOKNc3fKk1ibnZ7I/lZp2mt2vYSOkrl7hk+ZV14xxLukBUt2581Zo41F2Mw9Gid8Bs9T+8Est2S4eau9hbNDARus1U9saXk3M9q4GFta/DcCNuaMv8AObuso1AWQdwl1W90yHFc+2l+SUW8SuHt7x2SSrxAvME4XvHeMa+6FXm1zOF0MGn+NyXJXhxpxtloYQBhFWT9RcOrfwz+EpPwq5DnBpV1s+FtgOCdin/p8sZPwwGpQlZV7luf37IZ7M/gmvE7MseenJDaOZ/fivsYTjkSlHplalas8tWSB5ge/7+qNoWocCCJBGn/uCDtmw7STE/sH99QrBZUxz+9Po4T+qHJTTTNEtz2cYBICL4D2bYTqctrjiBc8sHJxb7GFcuylsSNR5YHnuT+HuvkKk5bLBeSMnVBVhwptGnBjUTqONuTW+gHvKn+MANI9VJxCrmB5ep3WljRk9B1P1JXcglixpAtFY7S0tDqfIHVBJI7wG4AyccxsqzdWet0NYdh3sBuc7t7u3gPomb7x1eu+p3gC4hjTypjDJB2xGOsnzMZZYJ/fXZc+WvUZNpcsCcqdeStVODtDmjXqyJER57K32lrppgNEADACXU7ZrXguIHhz9lZGPYWENIJhT6iWozxTknS81wKk5yVsot+12s5QrwURxmpDygW1ZSor4i0uCOpSBQz7UJxSYDusqWo5Id8U6Ntor1S2QlWiVY32ZULLXOQjjOL6YUZAfDeHSQ56sBrNY3CW1a+kQN0rr1nHcrHGUmG5OXAyqcUysSB7zKxF7ETfbQ8tqRD4IjKvVjwxrm7clX7ijD89U+4de6YBK5OpyOSTQiTTpiLtJwhzGktCopdmPFdm4i5r2HyXKn2ZNZ0DAKr0Ga4NS8DcLSsn4bakwrNRpvptncfgo+G2mB6J+XAsLT0S8uTdJt9CJy3SEFvxDvwTgqDj1wNMg5UN5ZPD4YJ8ZAAnxKBq8OqvcGkt85288b+Cp0+inlkskU2v0HDG5ciG5fJULArUzsc9+1Vk8gQ4Tz3Ex/wA9FFc9i7lg1N0Pbgy18QPvEPAx5TyXUenyx4aZZHgr7HkZG4V17NdpO6GPMOHsR1SSz7M1HOHxCGN8O870jA9/ReX3Zu5Y46GOqMGWvYASRvlgOoH0S8unk4/JGTp8F+uqTarZEfoq1WoFhgiOnQqLg/FK1Maa1Oowfeex7R7kQj+PXZFA1WQdLmkg7OaTpInl82/gt0WsyaWaxT5i3x+BcW4uvAvqggAxMdOg/MJ9wypqaI8PeSJn/VOeoSbhN3TuBDMOAksdGobZB5tzv45jmw4dFKoGHaRvtBIMZ8h6ALsZ9VGKTTtMpSskr2zRUcTg6iZ88z9V0XhFAUrdpI+zq8Zdn9B6Kl17TXXa375pg+oaD+avfFasN0jkJPmTAC4eBKeXcTY4vc/wxZoLnE+n6oTtXxFltavnDqrTTYOekgB7vZ0ebgnfCrcRqdgCSSdgBkklcl7Z1q/ELzRRB+Ez5ScNYzbW7w3PUl0cgqdRlc5bIjgrgV207CT4fvZM7u9dGluPL9Vrw3hjKLAxgkAS553cYy4/kOQWXFHn+z+iu0fpuKHymrf56RkMUU7fYvaTKPt7hwiN0DUqZwtmVi2YyeZ6HoF0csoQg3LhDnRLxO0DxrgTOUBS4XKku7p/TAQ9PjQbg7r5PUTjKbeJcEeTG0+hhT4dpQ10NJXv+LyMJfc3ZcVLtt8iaGFN4IUNd7YUDKgAQld/ihjip8HkCXdcAoNzwVtc0Ccpe4FpVsFwNik+gosWIb469R8jNrLzfVwcgoendqbj11Tc/SwYGJCAos5rj7FttkrjXA8ZfnQteD8PD3F0ZKWPdjCa9nrrSYKCKcU9pidIJqD4T4OxWt9dBo1/snkt+OVWvHiq9fV+60eP1VejwLPmjCXTfP6RuOG6aQZTqkkufnxEw3b29USynJME+QEnxILcdNiPJLbUu1AmfHcH3hPLeoDkST45jyD4H/Pkvvo4444KMFSR1NiiqQTbM0xqwI5lsD+ZpEj2Azy3Td5a5hDiC0tEmZnfMZnY5BccRMQEPZNc93d1HSM6ZwI5Ob3W7jonL7VrmaXNPhmQTnLX6oAyf0XN1eohiW6XgTK26KncXJqQAA1rcNbEQPNaUnvacZ9U4ueH6MgEt8ckevNb2NoAe81IjqcOWKknaYO1p0wKnxJw+YOHoSPovLmhb3DHMe2NQglh0nzMYnzCfG0pkfLCFuODtOWn3CXOGGfk9tRz677DVaX+ba1i57TLWkBjgP4XzpcfAhoInyMn99dVafisLK9P52kFuoTAe0H7JMzuJ9Fb69jUZlhPkHSPYpXeXGoFtRmYIDhhwnfB9PbZSZ8MlH48jI2iTsvda7imXnDGuG+5ILWz6Of7BWW5uDUqAA/M7Hpgfque8Oqmk496c4OxgbT7lOeHcWIOtz8NB9AB+im081ji3/AxxrktXa2+LGU7WnOuoJdBg6AYj/U6B5ByT0bYMboG2NUDLnYx5fl5yltjxIvrPr1MuqENadyymBDWtHlk9TPXLK5O0DSPHfy953388p+gkvebat+ANq7Zj3tg/UTtHU7T4fjhKbuoXnw5BGMLQN5Pj3YxyzgeCFDA524AGdxHuvpY8dmqgUsAElK6V8A/STjUXe6a3lVhYXF2BMM6+Lj+S5/c3Li4uJ3K5Gv1MM0Xijz9sH3It8eDpTazHtiQq3xWyaTIVctuJOaQCT7q28PeHt72Vwnj9rmx++MlTFltTIwUwZREIx1kAvHUgAlzW7mJPLTPtCW9qaUG24lF8StSdklNJ7Sn40qEvA12NNYhBV6YKg+ORut21k1JoXtcSL+7rETrWIrC3sms6spxReIVbksKYW10VLkx/QM4+UNXoqyrgeBS5taVlR+FPHH2mKaGN88uyDkJQa+ow7k4H8R+Y+i2ZeYMoHW41GhnzOcGidjqMZ8FVoW8WdSa6GYVtkmO2OBAnb0hPeFsY5svfHIABoIjwOSPEdNkjtLQskHrsOXijKHdkASOZ39jsF9wm5w+jpdot9i6k0NcwapdOtxJIIx3deCPCAR7J2ajS3V3p3J7x3iGy7vHwHd8NQVPtLrSd889PPYAAjMSMRHPkMnjiJ2LiR8ukGA3ViBykzk8p05klcvVaNZVtatfkS007Q9r0XH5NM9WwTtPzv5RnVjwBGUlu6zmH54EbhznAzsRqOkNMGCRmDAO62r8bZTt31qpJY3LgMlznEQ0DqXOETAxnYRyTtB2nq3NRzmk02T3WAwYiO84ZJMbbDAGwXAy+mwxS+Laf7Pb2+zo57RPbE6XjeXNId4fLpE+Eealb2mBE6H7x3SCDmJmIXE4R/DuH1KhJbDWj5nEwB4YyT4D6I4afI3UZN/wetfR2BnaKmdw8H+XV+CHu7qlUaYc0n2PscqnWNk1kF1as+Nxq0s/2mU2df0izSGiTjrM4xOR+4W5sOpxKw4pAF7auJ7hOcEHp1CPo8Lc9mHYIBcBhwA33BkLLduiHvdLSTgZ09Inlg+yuVhbsexrmxnI8ik6eG+Thl78M2TKhccNuGMJpS8R8zWtc7xBYZ+ghLLHtU9jtFcNe04nSGE556IXQLig6k4ubI69D4pXx7s9SvWF1MNp3G+o4a/q14HM/ejpyVXsTwS3RZPLdd2DMvKb26tBg9H/ANFHWqgjSBAPuVSLC9q21Q0ntcIdpc1wy09CFcA7AdyKzLq86W1y4ZPklNcXwRV7YEJBxLhHNqsgehb54iBuootp8CozceihVKBDoITXhV25hAnCYGy1HbCCu7QsyMhOlJSW2RZjyRf7LTRu9TUvvrstSzh95GETfHU1TKDhL8FW9tURs4oCYKYU2seOSp1wwgqWhfvZzVTxpq0DGfiRYrrhIOQlVTh5CntuNdUwp3TXrFuj2DKMZdCX4BXqe/BasW7kJ9tjn+0PgbGAVGAAzmOaotF0FNuPdpX3Lu9hgOB+qAtqYJScMJxx1MyQdbmVJcNwoGuh0BFPMtQriQiS5FFR8IL4jg4OG4II8wZCLujBS51TKpgqKILg6HbXTLlhfTnUMvZkuYesbFpOx91HXLojIwfrAM+cbqi0LpzHBzHuY4bOa4tI9QjT2nucg1A7l32U3EeIJbMrsYfUWo7Zqxqk1wWyzqlskcjE+fMeMQmVB8jAyQfSdz4GAQB+q56e0dzn/MBnkadKPQaYCKd2tr6NLWta/H+YBmAZwD3Qcb+wCcvUIPtM3cE9t+Luc82wd3WRrj7Tx1PNoBwOpKqcL0rehTL3NaN3ODR5uIA/FczJNzm2/IA04JwV1Y63AikDk7FxH2W/meXmrdUtmtaGtAAAw0cgmlOgykxrGzDGho8Y5x1JUNZoiNyd/wBPJdnT6eOOP58hUVy5MLW2bmTvy9cfomr7UO3/AHuonW2Z8foNvxTJYk3bPWGUXyHDpkD+Uxj0/FO+ztcteWBw0wHNG3XUG/w5yB02GVz/AInxF1OozQc0ySfHVuPZWrh1w2qGVqYhwzjdrhuPVfPa+1qd8fFIxN3R011u2qwcyB7jmFWbq1fTdqbMD8EfwniwJI2e2C5ng7Z7fA/RMLyq1/SFZgmssftf0ZLgpnHuAMvCyvTj4rcPG3xGgd0/ztiPEHwCT8auTbNjeMRt9ORVzL202vcBnlHPpHiqB2yrG4DXMb3mHvtAkuB+2CPmEjbfMxElIz6WP8i3FM1o8UY9uppzzCja4vKqQc5hBy0+IIn3Vm4JcNeN4eOSgnj2coTPFXKHtCmAIUVzaAg4lbsf7qYP5FIuxF0Vmtw6DLVtSOIKf1bechL69oD4Fe3WqZRjz0+Sv8Ro80me5Wa/pGMqt16eVThlxRW+eURB6Kt7otQvw1u1qeCOGcUwvUoWIdsfoK2FvHMImwrZyiuL8Br2ziKjTH3gMf0QlqN0lTjJWnaBlFNBbXS4ovXhJW1yHHzRYqmJgx1hBKAlxIL9KHnKY3NSUvcMp8OEMiqRKwKF6nbsoHo0ajxYvF6AiNPQE17NWmu4Z0Z3z/p2/wCqEqCt3YunDaj+ZLWA+AEn8QqNNDflSf8A6jV2WeSclRu6/uOq1fUzpHqVpWeNv3jkvoA2a1DMDrv5fv8AFC3N2xgLnmMqDinEG0hqOXHYdfD8FTru7fUcXPM+HIeSj1OqjiW1csFkl9XD3ve2QCcTvsB+Sa9leL/3erDvkfhw6Hk5V9pRNMSuHOTk235BOvigTUY5jjDmOaY5/ck9JefonFNroOoZjEehj/aQfdU/sPdvLIJkMe0A9AWuPsHBnsr1TZg5yACJ/ga1pB89Qb5SlTw54w34HT548MJSjdSFjrKAQCTLi6DBBECWwccpHql/EeAMe4ERJ22BztpcSJ2PddnxKslS3BlsnMwYyCJO3WMx4PCVXzjBY4NMz3j8p57zmZmD11S0hyz0155ZZPN26NyVS2lYq8E0Y1ucJ5jbP22OA07dTKXX/A2EF1NwZWGWho0h/wDC5kCCesb7ym1zXLXaYiJxJlvUZyOe0HmZ3Sqs+DI585wPXIPuvo5aeM4U0DtAOGcTDxDsPCbMfyKrXH6OlzarcEmHRjP2X+uQZ5gdUVwri4eND8O5Hqvm9VpXjk6JcuLzEsrHrWtRnIQrHnYoqnVUV3wTAFzQBbBCqnELNzTthXutSnZLrigDhwRwntY6GZx4fRR/hnotvhJ5fWgZkDCX6mqxTtWimM7AtKxGaAsXtxu5H0txHhbKrSHtB9FVq/YGgZhseSsdPtBSd9r0QFx2qpNJAIMLhSpO4MJzh9iq1/s9t2mS0E+OURxPsXTqMLGgAbYxCK4R2sp1HlpMdPFNrrjVJm7gmqXFt8gpxfNnLrj+yt8mKhjyCpnaPsw62cO8XjyXda3HGOHdcEju7enVMvIJT8efInbfAEsiXRws0XR8p9ioHUnfdPsV28cApE7Bbjs7S+6PZUrVfgH3fwcMFJ33T7Lb4Tvun2XbKvZyl90eyHf2ep/dC3/Vfg33fwcdZRcXBsQSQM7CTGV0SjQZQphjdm4n7x5n3RXEeA0w0wAl9+MsH8DfUxk/RdX0vPGc2q5oPHkUnR5SeSSTz/YCH4nxFtJknLpw3qR/X8EUWEABozueg6z+CT/4aXvJcZKu1eujhW1d/wBBSyRjwVu5rve4veZJ+ngFpSZJhWt/BAELU4TGQuE9QpO2L96IsrcNAbIKFY0gp2+m6IKHdb+CFZvsxZC29gqoNN7f/sb7Oa1h+hcrfbXU96YALsctLnkt8/l+qo/Yd7QXsMg6mvEdCCxxnwLmK3UyC3ujGlr3csDW8fiwLt6VRliQ6NSGT7+YMkHS2f8AyI8Wuh3jqeOaDq1tc8gfmA5RJ7pIwQZLfAnYShbmuQJHJ7hk76STA5TpJCWm5c1zT9mdLusGC109Ygz5clTHTrtBbBfftPynYAw49ASBAM4xsflnPUA1HFstcBt5TzkYP57prdQ6SC2DkEbA7Fp8CYjoCCdylVZmoaTiCIxkeE8hnb8FZXAyuAdtFj2ljhDXYnpJ+bzBz6KrNpuY9zHYcxxaY5OaYMeoVrqsgE7OG/j5jly8EBxigPjl0fO1j89S0B5/3hy5HqMKSl/AtxthHDeKB3cfg8im7X9fQqoXFJOuE3eoBjznkVwc2NP5ImzYG/lEfsqr2ozUEICQYPupm1IUyd8Mk/YFc0dwVW73h5aSRsrjVZrHil1RnJyZDI4/objntfPRVfdYmtxYd4rxUe5EtuBbXVkLVqrV4I5oZ5K5aijnUb/FgyDBXlxdvf8AM8mPFCvJUDnFMUUzUGi5eNnH3UlPiNRpnUUpdVK1/vCP22bRZqXaN7dwi29ro3lUt1wVC55K1YQlFnSKXapjuYRLeMMdzC5lSI5oltSNiVkoV0Y7LxxK7aW4KX07VrwHTkCB7k/mqw6u4/aU1HiT24TcOWeF7oPk2LcXaLPWphjCBz3PVLrAZJS2pxcuEFa2/FdK1znNuUuWzGm3Y9quQlQhAO4wCo3cTasUWeUWEVGhB1WBeOv2lROuWnmmqIW1m9s4seHt3H1HMK7Wjw+lraSNTCI9GNLfIBjh4qjfEHVP+znEYBouPPW3/wAh6CSPNy6Xp+bZPa3w/wCx+GW2VPobXToME7kH3j/2+iDq1RBnIJnnsZMe0+wU1zUnM9QP9uPqlz6m8f8AH2h9Ggeq+kj0XoGfVLZa6SDOf5cB31M9dXkva0uAcDkYPj6fl4LKkETz/AjBHkRB/qtbSq13dnO0bGOXt+S210eVdEjGbHl+E/lhLu0bQx9MD/4/Ya3x6bwrMy0MCBOYjmZ6fvGFWu0NIPrPLHSGwwHroEGPCdR9Vy/UpLYo+bE5HTENa46rehcjkYKjq0iMFQGkuHS6YCyNFrsL8PGl+45o/XyKpdF7mnBVi4ffB40uw4KbNi8xJs0FLmI0bUheXDNQkbocv5FStep074ZME8LtdTCejiPoP1WJtwlg+GD1JP5fksSnJ2eoacd7NOGaYHlCQV+AVmtnRPgF2WoxsIapRacEBBKMsfDaZc8MWcM4hQ+GQHiJQLnN6rsXGeAUqpGpoVC43/Z28EuoOIG8HI9EePJBupcf0L9heGVGs4IN6l4hwa5ouLXMc7xAwlrq7gYcCD0KvhjTVxdme00Fkr0IaneAbqdt00rXCSPOEjYFe6lr8RpXsjqhpg7WbB6z4i0I8VrlZSPUSF60cVqStZWpI9R44LQhbErESCRGWnqoyHdVMV4mJsJMiFRwUtK8c0gyQQZBHIjYheELRzFu5eQrTLDacfkBr+6RkOAwT/E0bebfZGvrhw1DYzkEEDmI5T3R7KngKSm9zflcR1gkT5wuhh184Kpcr/sOM2iwuquEgbH/AI9IUFcM0y4lrhkR8x6QOXmlLbp/33/73fqsawlHk9TbVRX/ACa8xauIdpQGaKDjLh3qkFpAO7WA7OI3dy2HVV+hWLdtkN8IrZuFBlyyyS3SfIpy3O2MXBrwgq9qRstQ8ypRdcisTvsJP7A4WzHOBBG4RLmgrQthDKP0ea+h3aV9bf4gp2uwkNtcaHSPVO2PDoI5qPNjr5ImnCuS2WIimwfwheo3+7GG4PyjksXO3GbJfRf65yvH8lixBl7LGCXWyMt/lCxYvPsyPYs4vSbJwPYLmnb22Z8MnQ2Z30ifdYsVGn/3EEcxcvAsWLuo8SBS01ixDIxkzURQWLEiQtmO3Ub1ixAARleLFi1GnixYsRI8YvCsWLx40KwLFiJBompotixYhfYuRs5QOWLESPI0conbrFiJDIhFupysWJiGAtZOOBcv5h+KxYk5v8GLydHYrP5AsWLFwA10f//Z")
   
st.subheader('Prediction Probability')

st.subheader('Prediction Probability')
st.write(prediction_proba)
