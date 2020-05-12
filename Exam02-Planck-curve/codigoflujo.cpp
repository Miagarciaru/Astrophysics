#include <cmath>
#include <iostream>

double const h = 6.625;
double const k = 1.3806;
double const c = 2.99;
double const T = 6.000;

double planckiana(double lambda);

int main() {
  std::cout.precision(5);
  std::cout.setf(std::ios::scientific);

  double lambda = 0.1;
  double dlamb = 0.1;
  double lamb_max = 5.0;

  for (int ii = 0; lambda <= lamb_max; lambda += dlamb) {
    std::cout << lambda << "\t" << planckiana(lambda) << "\n";
  }

  return 0;
}

double planckiana(double lambda) {
  double flux = 0.0;
  double coef = 0.0;
  double den = 0.0;
  double arg = 0.0;
  coef = (2*h*c*c)/(pow(lambda, 5));
  arg = (h*c)/(lambda*k*T);
  den = std::exp(arg) - 1.0;
  flux = coef/(10* den); // unidades cgs del libro

  return flux;
}
