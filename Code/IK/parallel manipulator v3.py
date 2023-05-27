# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:47:59 2022

@author: techv
"""


import numpy as np
import matplotlib.pyplot as plt
import math
const = math.pi/180

%matplotlib qt
x =   -100
y =   -100
z =  -275

theta = np.radians(0)  #angle wrt x
psi   = np.radians(0)  #angle wrt y
phi   = np.radians(0)  #angle wrt z

p = np.array([[x],
              [y],
              [z],
              [1]])

offdist = np.array([[  0],
                    [  0],
                    [ 50],
                    [  1]])

r = p[0:3] + offdist[0:3]

print(r)

x__ = r[0][0]
y__ = r[1][0]
z__ = r[2][0]

a,b,s = [0,0,0],[0,0,0],[0,0,0]

np.set_printoptions(formatter={'float_kind':'{:f}'.format})

R = 92    #distance of vertex in base
r = 65     #distance of vertex in end effector

#elements of roational matrices
r11 = math.cos(phi)*math.cos(theta)
r12 = math.cos(phi)*math.sin(theta)*math.sin(psi)-math.sin(phi)*math.cos(psi)
r13 = math.cos(phi)*math.sin(theta)*math.cos(psi)+math.sin(phi)*math.sin(psi)

r21 = math.sin(phi)*math.cos(theta)
r22 = math.sin(phi)*math.sin(theta)*math.sin(psi)+math.cos(phi)*math.cos(psi)
r23 = math.sin(phi)*math.sin(theta)*math.cos(psi)-math.cos(phi)*math.sin(psi)

r31 = -math.sin(theta)
r32 = math.cos(theta)*math.sin(psi)
r33 = math.cos(theta)*math.cos(psi)

#The transformation matrix
T = np.array([[r11,r12,r13,p[0]],
              [r21,r22,r23,p[1]],
              [r31,r32,r33,p[2]],
              [0  ,0  ,0  ,1  ]])

a[0]= np.array([[R*math.cos(30*const)],
                [-R*math.sin(30*const)],
                [0],
                [1]])

a[1]= np.array([[-R*math.cos(30*const)],
                [-R*math.sin(30*const)],
                [0],
                [1]])

a[2]= np.array([[0],
                [R],
                [0],
                [1]])

b[0]= np.array([[r*math.cos(30*const)],
                [-r*math.sin(30*const)],
                [0],
                [1]])

b[1]= np.array([[-r*math.cos(30*const)],
                [-r*math.sin(30*const)],
                [0],
                [1]])

b[2]= np.array([[0],
                [r],
                [0],
                [1]])

Rt = 0
ans = []
s_ = [0,0,0]
r_ans = []

#inverse kinematics part
for i in range(3):
    s[i] = np.dot(T,b[i]) 
    s_[i] = s[i] - a[i]
    ans.append(math.sqrt(np.square(s[i][0])+np.square(s[i][1])+np.square(s[i][2])))
    r_ans.append(math.sqrt(np.square(s_[i][0])+np.square(s_[i][1])+np.square(s_[i][2])))    

activate = 0
print("r_ans",np.round(r_ans,2),"\n")

def cal_xyz(a,s):
    A  = np.zeros((3))
    B  = np.zeros((3))
    C  = np.zeros((3))
    D  = np.zeros((3))
    x_ = np.zeros((3))
    y_ = np.zeros((3))
    z_ = np.zeros((3))
 
    l,m,n = np.zeros((3)),np.zeros((3)),np.zeros((3))

    for i in range(3):     
        
        l[i] = s_[i][0][0]
        m[i] = s_[i][1][0]
        n[i] = s_[i][2][0]
        
        x_[i] = a[i][0][0]
        y_[i] = a[i][1][0]
        z_[i] = a[i][2][0]
        
        A[i] = +2*m[i]*n[i]
        B[i] = -1*n[i]*l[i]
        C[i] = -1*m[i]*l[i]
        D[i] = 1*(-2*m[i]*n[i]*x_[i] + n[i]*l[i]*y_[i] + m[i]*l[i]*z_[i]) 
        
    a_ = np.array([[A[0],B[0],C[0]],
                   [A[1],B[1],C[1]],
                   [A[2],B[2],C[2]]])
    
    b_ = np.array([[D[0]],
                   [D[1]],
                   [D[2]]])   

    link_v = np.array([[l[0],l[1],l[2]],
                       [m[0],m[1],m[2]],
                       [n[0],n[1],n[2]]])
    print(np.dot(np.transpose(b_),np.linalg.inv(a_)),"\n")
    return(link_v,np.dot(np.linalg.inv(a_),b_))

def comp_F(RM):
    ra,rs,rl = np.array([[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]),np.array([[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]),np.array([[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]])
    ANS = [] 
    for i in range(3):
        ra[i] = a[i][0:3]-p[0:3]
        rs[i] = s[i][0:3]-p[0:3]
        rl[i] = -ra[i]+rs[i]
        
    rs_arr = [rs[0][1]+rs[1][1],rs[0][0]]
    RM = np.transpose(RM)
    
    F1az  = RM[0]/(2*(rs_arr[0]))
    F1bz = RM[1]/(2*(rs_arr[1]))
    
    F1 = np.array([[0],[0],[F1az + F1bz]])
    F2 = np.array([[0],[0],[F1az - F1bz]])
    F3 = np.array([[0],[0],[F1az]])
    
    
    MUV_2 = F1/np. linalg. norm(F1)
    LUV_2 = rl[0]/np.linalg.norm(rl[0])
    dot_product = (np.dot(np.transpose(MUV_2), LUV_2))
    # print(np.arccos(dot_product[0][0][0]))
    angle1 = np.arccos(dot_product[0][0][0])
    
    MUV_2 = F1/np.linalg.norm(F1)
    LUV_2 = rl[1]/np.linalg.norm(rl[1])
    dot_product = np.dot(np.transpose(MUV_2), LUV_2)
    angle2 = np.arccos(dot_product[0][0][0])
    
    MUV_2 = F1/np.linalg.norm(F1)
    LUV_2 = rl[2]/np.linalg.norm(rl[2])
    dot_product = np.dot(np.transpose(MUV_2), LUV_2)
    angle3 = np.arccos(dot_product[0][0][0])
    
    print(np.degrees(angle1),np.degrees(angle2),np.degrees(angle3), "\n")
    F1 = F1[2]/np.cos(angle1)
    F2 = F2[2]/np.cos(angle2)
    F3 = F3[2]/np.cos(angle3)
    return([F1,F2,F3,angle1,angle2,angle3])

# def cal_central_angles():
#     xAxis = np.array([1,0,0])
#     yAxis = np.array([0,1,0])
#     #p_3axis = np.array([r[0][0],r[1][0],r[2][0]]) 
#     p_3axis = np.array([x__,y__,z__])
#     magX =  np.linalg.norm(p)*np.linalg.norm(xAxis)
#     magY =  np.linalg.norm(p)*np.linalg.norm(yAxis)
    
#     alpha = np.degrees(np.arcsin(np.linalg.norm(np.cross(p_3axis,xAxis))/magX))
#     beta  = np.degrees(np.arcsin(np.linalg.norm(np.cross(p_3axis,yAxis))/magY))
    
#     print(np.linalg.norm(np.cross(p_3axis,xAxis)))
#     print(magX)
#     print(np.linalg.norm(np.cross(p_3axis,xAxis))/magX)
#     if x > 0 and y > 0:
#         alpha = alpha
#         beta = beta
#     elif x < 0 and y > 0:
#         alpha = 180 -  alpha
#     elif x < 0 and y < 0:
#         alpha =  180 - alpha
#         beta  =  180 - beta
#     elif x > 0 and y < 0:
#         beta = 180 - beta
        
#     print('alpha' , alpha)
#     print('beta'  , beta)
#     print('x', x)
#     print('y', y)
#     print('z', z)

def cal_central_angles():
    xAxis = np.array([1,0,0])
    yAxis = np.array([0,1,0])
    #p_3axis = np.array([r[0][0],r[1][0],r[2][0]]) 
    p_3axis = np.array([x__,y__,z__])
    magX =  np.linalg.norm(p[0:3])*np.linalg.norm(xAxis)
    magY =  np.linalg.norm(p[0:3])*np.linalg.norm(yAxis)
    
    alpha = np.degrees(np.arccos((np.dot(p_3axis,xAxis))/magX))
    beta  = np.degrees(np.arccos((np.dot(p_3axis,yAxis))/magY))
    
    print(np.dot(p_3axis,xAxis))
    print(np.dot(p_3axis,yAxis))   
    print('alpha' , alpha)
    print('beta'  , beta)
    print('x', x)
    print('y', y)
    print('z', z)
    return alpha,beta
    
    
def cal_M(F1,F2,F3,W,r,R):
    M1 = np.cross(r[0]-np.transpose(p[0:3]),F1)
    M2 = np.cross(r[1]-np.transpose(p[0:3]),F2)
    M3 = np.cross(r[2]-np.transpose(p[0:3]),F3)
    
    MW = np.cross([0,0,0],W)
    #AM = AMX + AMY + AMZ
    AM = -(MW+M1+M2+M3)
    print("\n", "MW",MW)
    print("M1",M1)
    print("M2",M2)
    print("M3",M3,"\n")
    print("Sum of all Moments : ",AM+MW+M1+M2+M3,"\n")
    
    return AM
    
def cal_F(u1,u2,u3,W):
    # Rx + W[0] + u1[0]*F1 + u2[0]*F2 + u3[0]*F3 = 0 #X values
    # Ry + W[1] + u1[1]*F1 + u2[1]*F2 + u3[1]*F3 = 0 #Y values
    # Rz + W[2] + u1[2]*F1 + u2[2]*F2 + u3[2]*F3 = 0 #Z values
    
    A = np.array([[u1[0], u2[0], u3[0]],
                  [u1[1], u2[1], u3[1]],
                  [u1[2], u2[2], u3[2]]])
    B = np.array([W[0],
                  W[1],
                  W[2]])
    
    F_mag = np.dot(np.linalg.inv(A),B)
    F1 = u1*F_mag[0]
    F2 = u2*F_mag[1]
    F3 = u3*F_mag[2]
    R = - (W+F1+F2+F3)
    print(F1)
    # print("Force:",W+F1+F2+F3)
    print("\n"," W", W)
    print("F1",F1)
    print("F2",F2)
    print("F3",F3)
    print("Reaction Force:", R, "\n")
    #Reaction force = [0 0 30]
    return R,F1,F2,F3

def main():
    for i in range(3):
        if r_ans[i] > 360 or r_ans[i] < 240:
            print("configuration not possible please try again")
            activate = 0
            break
        else:
            activate = 1
    if activate == 1:        
        fig = plt.figure(figsize = (9,9))
        axs = fig.add_subplot(111, projection='3d')
        
        #axs.plot([Rt[0][0],Rt[1][0],Rt[2][0]],[Rt[0][1],Rt[1][1],Rt[2][1]],[Rt[0][2],Rt[1][2],Rt[2][2]])
        
        axs.plot([0,a[0][0],a[1][0],s[1][0],s[2][0],p[0],offdist[0][0]],
                 [0,a[0][1],a[1][1],s[1][1],s[2][1],p[1],offdist[1][0]],
                 [0,a[0][2],a[1][2],s[1][2],s[2][2],p[2],offdist[2][0]],linewidth = 5,color ="black")
        
        axs.plot([0,a[1][0],a[2][0],s[2][0],s[0][0],p[0]],
                 [0,a[1][1],a[2][1],s[2][1],s[0][1],p[1]],
                 [0,a[1][2],a[2][2],s[2][2],s[0][2],p[2]],linewidth = 5,color = "black")
        
        axs.plot([0,a[2][0],a[0][0],s[0][0],s[1][0],p[0]],
                 [0,a[2][1],a[0][1],s[0][1],s[1][1],p[1]],
                 [0,a[2][2],a[0][2],s[0][2],s[1][2],p[2]],linewidth = 5,color = "black")
        
        
        axs.plot([offdist[0][0],0],
                 [offdist[1][0],0],
                 [offdist[2][0],0],linewidth = 5,color ="red")
        
        
        axs.plot([offdist[0][0],p[0]],
                 [offdist[1][0],p[1]],
                 [offdist[2][0],p[2]],linewidth = 5,color ="green")
        
        
        axs.plot([offdist[0][0],p[0]],
                 [offdist[1][0],p[1]],
                 [offdist[2][0],p[2]],linewidth = 5,color ="green")
        
        axs.plot([0,p[0]],
                 [0,p[1]],
                 [0,p[2]],linewidth = 5,color ="yellow")
        
        #axs.axes.set_xlim3d(left=-100, right=100) 
        #axs.axes.set_ylim3d(bottom=-100, top=100)     
        
        axs.set_xlabel('X axis')
        axs.set_ylabel('Y axis')
        axs.set_zlabel('Z axis')
        
        #print(a[0],"\n\n",a[1],"\n\n",a[2]) #a = base points
        #print(s[0],"\n\n",s[1],"\n\n",s[2]) #s = vector
        link_v,wow = cal_xyz(a,s)
        # plt.show()
        wow = wow *-1
        S = np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                S[i][j] = np.array(s[i][j])
        
        axs.plot(s[0][0], s[0][1], s[0][2],"ro")
    
        axs.plot(s[1][0], s[1][1], s[1][2],"go")
        
        axs.plot(s[2][0], s[2][1], s[2][2],"bo")
        
        axs.plot(p[0],p[1],p[2],"yo")
        
        cal_central_angles()
        
        # np.linalg.norm(link_v[:][0])
        # link_v_ = np.transpose(link_v)
        # #print(wow)
        # v1 = link_v_[0]
        # v2 = link_v_[1]
        # v3 = link_v_[2]
        
        # u1 = v1/np.linalg.norm(v1)
        # u2 = v2/np.linalg.norm(v2)
        # u3 = v3/np.linalg.norm(v3)
        
        # #print(u1)
        # W = [0,0,-2.45]
        # R,F1,F2,F3 = cal_F(u1,u2,u3,W)
        
        # RM = cal_M(F1,F2,F3,W,S,R)
        
        # print("Reaction Moment :", RM)
        
        # RF = np.squeeze(np.array(comp_F(RM)))
        
        # print("\n"+"F in link1 :", (F1[2]/abs(F1[2]))*np.linalg.norm(F1))
        # print("F in link2 :",      (F2[2]/abs(F2[2]))*np.linalg.norm(F2))
        # print("F in link3 :",      (F3[2]/abs(F3[2]))*np.linalg.norm(F3),"\n")
        
        # print("Reaction in link1 :", RF[0])
        # print("Reaction in link2 :", RF[1])
        # print("Reaction in link3 :", RF[2],"\n")
        
        # print("Total in link1 :", (F1[2]/abs(F1[2]))*np.linalg.norm(F1)+RF[0])
        # print("Total in link2 :", (F2[2]/abs(F2[2]))*np.linalg.norm(F2)+RF[1])
        # print("Total in link3 :", (F3[2]/abs(F3[2]))*np.linalg.norm(F3)+RF[2])
        
        # axs.plot(p[0],p[1],p[2],"white")

        
if __name__ == "__main__":
    main()