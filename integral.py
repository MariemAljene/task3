from flask import Flask, jsonify

import math
app = Flask(__name__)
def numerical_integration(lower,upper,n): 
    dx=(upper-lower)/n
    integral=0.0
    for i in range(n):
        x=lower+(i+0.5)*dx
        integral+=abs(math.sin(x))*dx
    return integral
@app.route('/numericalintegral/<float:lower>/<float:upper>', methods=['GET'])
def numerical_integral(lower, upper):
    print(f"Route hit with lower={lower} and upper={upper}")
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    results = []

    for n in n_values:
        integral = numerical_integration(lower, upper, n)
        results.append({'n': n, 'integral': round(integral, 10)})
    return jsonify({'lower': lower, 'upper': upper, 'results': results})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

