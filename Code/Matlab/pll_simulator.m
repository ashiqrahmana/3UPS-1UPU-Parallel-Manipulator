% pll-maipulator workspace analysis

hold off ;
clc ;
lmin = 800 ;
lmax = 1400 ;
R = 150  ;  #distance of vertex in base
r = 60  ;   #distance of vertex in end effector

const = pi/180  ;


phi   = 0*const ; #angle wrt z
theta = 0*const ; #angle wrt x
psi   = 0*const ; #angle wrt y

st1 =  1*const ; #code functional parameters
st2 =  1*const ; #code functional parameters
end1 = 1*const ; #code functional parameters
end2 = 1*const ; #code functional parameters


 hold on ;
 grid on ;
 axis equal ;

 for xp = -1500 : 100 : 1500
    for yp = -1500 : 100 : 1500
        for zp = -1400 : 100 : -400
                  cv = 1;

              for theta =  0 : st1 : end1
                if cv==0
                  break
                  end
                   for psi = 0 : st2 : end2

                    #elements of roational matrices
                    r11 = cos(phi)*cos(theta) ;
                    r12 = cos(phi)*sin(theta)*sin(psi)-sin(phi)*cos(psi) ;
                    r13 = cos(phi)*sin(theta)*cos(psi)+sin(phi)*sin(psi) ;

                    r21 = sin(phi)*cos(theta) ;
                    r22 = sin(phi)*sin(theta)*sin(psi)+cos(phi)*cos(psi) ;
                    r23 = sin(phi)*sin(theta)*cos(psi)-cos(phi)*sin(psi) ;

                    r31 = -sin(theta) ;
                    r32 = cos(theta)*sin(psi) ;
                    r33 = cos(theta)*cos(psi) ;

                    #Homogenous Transformation Matrix
                    k = [r11 r12 r13 xp; r21 r22 r23 yp; r31 r32 r33 zp;0 0 0 1] ;

                    #Inverse Kinematics Calculations
                    aa1 = [ R*cos(30*const) ; -R*sin(30*const) ; 0 ; 1] ;
                    aa2 = [-R*cos(30*const) ; -R*sin(30*const) ; 0 ; 1] ;
                    aa3 = [0 ; R ; 0 ; 1] ;

                    bb1 = [r*cos(30*const) ; -r*sin(30*const) ;  0  ;  1] ;
                    bb2 = [-r*cos(30*const) ; -r*sin(30*const) ;  0  ;  1] ;
                    bb3=  [0  ;  r  ;  0 ;  1] ;

                    res1 =  k*bb1 ;
                    res2 =  k*bb2 ;
                    res3 =  k*bb3 ;

                    g1 = res1 - aa1 ;
                    g2 = res2 - aa2 ;
                    g3 = res3 - aa3 ;

                    en1 = g1.^2 ;
                    en2 = g2.^2 ;
                    en3 = g3.^2 ;

                    sum1 = sum(en1) ;
                    sum2 = sum(en2) ;
                    sum3 = sum(en3) ;

                    len1 = (sum1)^(1/2);
                    len2 = (sum2)^(1/2);
                    len3 = (sum3)^(1/2);

                  #Setting limits reference to actual model
                  if(len1 >= lmin ) && (len2 >= lmin ) && (len3 >= lmin ) && (len1 <= lmax ) && (len2 <= lmax ) && (len3 <= lmax )
                   cv = 1 ;
                   else
                  cv = 0 ;
                  break
                 end
          end
       end
        #Visualisations
        if (cv == 1)
             scatter3(xp,yp,zp,"b" ,"filled") ;
             title ("Parallel Manipulator Workspace");
        end
     end
   end
 end
   printf("done") ;
