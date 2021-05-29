import csv
#-------------------------------------------------------------------------------
def dSdt(beta, gamma, N, t_n, s_n, i_n):
  return (-beta*i_n*s_n)/N

def dIdt(beta, gamma, N, t_n, s_n, i_n):
  return ((beta*i_n*s_n)/N)-gamma*i_n

def dRdt(beta, gamma, N, t_n, s_n, i_n):
  return gamma*i_n
#-------------------------------------------------------------------------------
def Runge_Kutta(beta, gamma, N, dF, F, t_n, s_n, i_n, r_n, dt):

    k1 = dF(beta, gamma, N, t_n, s_n, i_n)
    k2 = dF(beta, gamma, N, t_n + dt/2, s_n + dt*k1/2, i_n + dt*k1/2)
    k3 = dF(beta, gamma, N, t_n + dt/2, s_n + dt*k2/2, i_n + dt*k2/2)
    k4 = dF(beta, gamma, N, t_n + dt, s_n + dt*k3, i_n + dt*k3)

    F_n_plus_one= F[-1] + dt/6*(k1 + 2*k2 + 2*k3 + k4)

    F.append(F_n_plus_one)
#-------------------------------------------------------------------------------
def Create_Table(T, S, I, R):

    myFile = open('Tabla_SIR.csv', 'w')
    with myFile:

      writer = csv.writer(myFile)
      writer.writerow(["t", "S(t)", "I(t)", "R(t)", "N"])

      for t_n in T:
          writer.writerow([t_n, S[t_n], I[t_n], R[t_n], S[t_n]+I[t_n]+R[t_n]])

#-------------------------------------------------------------------------------
