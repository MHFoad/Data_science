import numpy as np
#import scipy.linalg

def vector_angles(X, Y):
    inner_product = np.sum(X*Y, axis=1)
    X_norms=np.sqrt(np.sum(X**2,axis=1))
    Y_norms = np.sqrt(np.sum(Y ** 2, axis=1))
    cosine_angle=inner_product/(X_norms*Y_norms)
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)  # Clip to avoid precision errors


    angle_rad=np.arccos(cosine_angle)
    angle_deg=np.degrees(angle_rad)
    return(angle_deg)


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 5))
    b= np.random.randint(0, 11, (4, 5))
    print(a,"\n")
    print(b,"\n")
    print(vector_angles(a,b))

if __name__ == "__main__":
    main()
