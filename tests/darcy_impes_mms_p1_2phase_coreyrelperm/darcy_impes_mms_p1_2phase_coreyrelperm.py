# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.

from numpy import sin, cos, pi, exp, sqrt

py_dict = {
    "domain_extents" : (1.0, 1.2, 0.8, ),

    "finish_time" : 1.0,

    "pressure1_scale" : 100000.0,

    "saturation2_scale" : 0.1,

    "gravity_magnitude" : 1.0,

    "viscosity1" : 1.725e-05,

    "viscosity2" : 0.001,

    "density1" : 1.284,

    "density2" : 1000.0,

    "permeability1" : lambda (s1, s2): 1.567346939e-9*(1.05263157894737*s1 - 0.0526315789473684)**4,

    "permeability2" : lambda (s1, s2): 1.567346939e-9*(-1.05263157894737*s1 + 1.05263157894737)**2*(-(1.05263157894737*s1 - 0.0526315789473684)**2 + 1.),

    "porosity" : 0.4,

    "absolute_permeability" : 1.567346939e-09,

    "gravity_direction_1D" : 1,

    "pressure_1D" : lambda x, t: (25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*x),

    "saturation1_1D" : lambda x, t: 1. - 0.1*exp(-1.0*x)/(1.0*t + 1.),

    "saturation2_1D" : lambda x, t: 0.1*exp(-1.0*x)/(1.0*t + 1.),

    "darcy_velocity1_magnitude_1D" : lambda x, t: 9.0860692115942e-5*((1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**8)**(1/2.)*abs(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x) - 1.284),

    "source_saturation1_1D" : lambda x, t: 9.0860692115942e-5*pi**2*(1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**4*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*x) - 3.82571335225019e-5*(1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**3*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x) - 1.284)*exp(-1.0*x)/(1.0*t + 1.) + 0.04*exp(-1.0*x)/(1.0*t + 1.)**2,

    "darcy_velocity2_magnitude_1D" : lambda x, t: 1.567346939e-6*((1.11022302462516e-16 + 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**4*(-(1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**2 + 1.)**2)**(1/2.)*abs(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x) - 1000.0),

    "source_saturation2_1D" : lambda x, t: 3.29967776631579e-7*(1.11022302462516e-16 + 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**2*(1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x) - 1000.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.567346939e-6*pi**2*(1.11022302462516e-16 + 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**2*(-(1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*x) + 3.29967776631579e-7*(1.11022302462516e-16 + 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x) - 1000.0)*(-(1.0 - 0.105263157894737*exp(-1.0*x)/(1.0*t + 1.))**2 + 1.)*exp(-1.0*x)/(1.0*t + 1.) - 0.04*exp(-1.0*x)/(1.0*t + 1.)**2,

    "gravity_direction_2D" : (1, 0, ),

    "pressure_2D" : lambda x, y, t: (25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x),

    "saturation1_2D" : lambda x, y, t: -0.15625*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1,

    "saturation2_2D" : lambda x, y, t: 0.15625*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.),

    "darcy_velocity1_magnitude_2D" : lambda x, y, t: (8.25566537178801e-9*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2 - 1.284)**2*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**8 + 2.29324038105222e-8*pi**2*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**8*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x)**2*cos(0.833333333333333*pi*y)**2)**(1/2.),

    "source_saturation1_2D" : lambda x, y, t: -5.97767711289092e-5*y**2*(-2.5*y + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2 - 1.284)*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**3*exp(-1.0*x)/(1.0*t + 1.) + 0.0625*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 0.000151434486859903*pi*(1.64473684210526*y**2*exp(-1.0*x)/(1.0*t + 1.) - 1.31578947368421*y*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**3*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)*cos(1.0*pi*x)*cos(0.833333333333333*pi*y) + 0.000217056097832528*pi**2*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x) - 0.000126195405716586*pi**2*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*x)*cos(0.833333333333333*pi*y)**2,

    "darcy_velocity2_magnitude_2D" : lambda x, y, t: (2.45657642719267e-12*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2 - 1000.0)**2*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)**2 + 6.82382340886853e-12*pi**2*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x)**2*cos(0.833333333333333*pi*y)**2)**(1/2.),

    "source_saturation2_2D" : lambda x, y, t: 5.15574650986842e-7*y**2*(-2.5*y + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2 - 1000.0)*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*exp(-1.0*x)/(1.0*t + 1.) + 5.15574650986842e-7*y**2*(-2.5*y + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2 - 1000.0)*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-1.0*x)/(1.0*t + 1.) - 0.0625*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 2.61224489833333e-6*pi*(-0.822368421052632*y**2*exp(-1.0*x)/(1.0*t + 1.) + 0.657894736842105*y*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)*cos(1.0*pi*x)*cos(0.833333333333333*pi*y) + 2.61224489833333e-6*pi*(0.822368421052632*y**2*exp(-1.0*x)/(1.0*t + 1.) - 0.657894736842105*y*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)*cos(1.0*pi*x)*cos(0.833333333333333*pi*y) + 3.74421768761111e-6*pi**2*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x) - 2.17687074861111e-6*pi**2*(0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.164473684210526*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*x)*cos(0.833333333333333*pi*y)**2,

    "gravity_direction_3D" : (1, 0, 0, ),

    "pressure_3D" : lambda x, y, z, t: (25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2*cos(1.0*pi*x),

    "saturation1_3D" : lambda x, y, z, t: -0.54931640625*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1,

    "saturation2_3D" : lambda x, y, z, t: 0.54931640625*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.),

    "darcy_velocity1_magnitude_3D" : lambda x, y, z, t: (8.25566537178801e-9*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2 - 1.284)**2*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**8 + 5.15979085736751e-8*pi**2*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**8*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*y)**4*sin(1.25*pi*z)**2*cos(1.0*pi*x)**2*cos(1.25*pi*z)**2 + 2.29324038105222e-8*pi**2*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**8*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**4*cos(1.0*pi*x)**2*cos(0.833333333333333*pi*y)**2)**(1/2.),

    "source_saturation1_3D" : lambda x, y, z, t: -0.000210152711000071*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2 - 1.284)*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**3*exp(-1.0*x)/(1.0*t + 1.) + 0.2197265625*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 0.000227151730289855*pi*(8.67341694078947*y**2*z**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 4.62582236842105*y**2*z*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**3*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)*cos(1.0*pi*x)*cos(1.25*pi*z) - 0.000151434486859903*pi*(5.78227796052632*y**2*z**2*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 4.62582236842105*y*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**3*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)**2*cos(1.0*pi*x)*cos(0.833333333333333*pi*y) + 0.000500995760694847*pi**2*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2*cos(1.0*pi*x) - 0.000283939662862319*pi**2*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x)*cos(1.25*pi*z)**2 - 0.000126195405716586*pi**2*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.25*pi*z)**2*cos(1.0*pi*x)*cos(0.833333333333333*pi*y)**2,

    "darcy_velocity2_magnitude_3D" : lambda x, y, z, t: (2.45657642719267e-12*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2 - 1000.0)**2*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)**2 + 1.53536026699542e-11*pi**2*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*y)**4*sin(1.25*pi*z)**2*cos(1.0*pi*x)**2*cos(1.25*pi*z)**2 + 6.82382340886853e-12*pi**2*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**4*cos(1.0*pi*x)**2*cos(0.833333333333333*pi*y)**2)**(1/2.),

    "source_saturation2_3D" : lambda x, y, z, t: 1.81256713237562e-6*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2 - 1000.0)*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*exp(-1.0*x)/(1.0*t + 1.) + 1.81256713237562e-6*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*x)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2 - 1000.0)*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-1.0*x)/(1.0*t + 1.) - 0.2197265625*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 3.9183673475e-6*pi*(-4.33670847039474*y**2*z**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 2.31291118421053*y**2*z*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)*cos(1.0*pi*x)*cos(1.25*pi*z) + 3.9183673475e-6*pi*(4.33670847039474*y**2*z**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 2.31291118421053*y**2*z*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)*cos(1.0*pi*x)*cos(1.25*pi*z) - 2.61224489833333e-6*pi*(-2.89113898026316*y**2*z**2*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 2.31291118421053*y*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)**2*cos(1.0*pi*x)*cos(0.833333333333333*pi*y) + 2.61224489833333e-6*pi*(2.89113898026316*y**2*z**2*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 2.31291118421053*y*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)**2*cos(1.0*pi*x)*cos(0.833333333333333*pi*y) + 8.64217687198611e-6*pi**2*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*sin(1.25*pi*z)**2*cos(1.0*pi*x) - 4.897959184375e-6*pi**2*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*y)**2*cos(1.0*pi*x)*cos(1.25*pi*z)**2 - 2.17687074861111e-6*pi**2*(0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.578227796052632*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.25*pi*z)**2*cos(1.0*pi*x)*cos(0.833333333333333*pi*y)**2,

    }

text_dict = {
    "DOMAIN_EXTENTS" : "1.0 1.2 0.8 ",

    "FINISH_TIME" : "1.0",

    "PRESSURE1_SCALE" : "100000.0",

    "SATURATION2_SCALE" : "0.1",

    "GRAVITY_MAGNITUDE" : "1.0",

    "VISCOSITY1" : "1.725e-05",

    "VISCOSITY2" : "0.001",

    "DENSITY1" : "1.284",

    "DENSITY2" : "1000.0",

    "PERMEABILITY1" : "1.567346939e-9*(1.05263157894737*s1 - 0.0526315789473684)**4",

    "PERMEABILITY2" : "1.567346939e-9*(-1.05263157894737*s1 + 1.05263157894737)**2*(-(1.05263157894737*s1 - 0.0526315789473684)**2 + 1.)",

    "POROSITY" : "0.4",

    "ABSOLUTE_PERMEABILITY" : "1.567346939e-09",

    "GRAVITY_DIRECTION_1D" : "1",

    "PRESSURE_1D" : "(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*X[0])",

    "SATURATION1_1D" : "1 - 0.1*exp(-1.0*X[0])/(1.0*t + 1.)",

    "SATURATION2_1D" : "0.1*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_MAGNITUDE_1D" : "9.0860692115942e-5*((1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**8)**(1/2.)*abs(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0]) - 1.284)",

    "SOURCE_SATURATION1_1D" : "9.0860692115942e-5*pi**2*(1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**4*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*X[0]) - 3.82571335225019e-5*(1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**3*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0]) - 1.284)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.04*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_MAGNITUDE_1D" : "1.567346939e-6*((1.11022302462516e-16 + 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**4*(-(1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)**2)**(1/2.)*abs(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0]) - 1000.0)",

    "SOURCE_SATURATION2_1D" : "3.29967776631579e-7*(1.11022302462516e-16 + 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**2*(1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0]) - 1000.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.567346939e-6*pi**2*(1.11022302462516e-16 + 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**2*(-(1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*X[0]) + 3.29967776631579e-7*(1.11022302462516e-16 + 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0]) - 1000.0)*(-(1.0 - 0.105263157894737*exp(-1.0*X[0])/(1.0*t + 1.))**2 + 1.)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.04*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "GRAVITY_DIRECTION_2D" : "1 0. ",

    "PRESSURE_2D" : "(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])",

    "SATURATION1_2D" : "-0.15625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.",

    "SATURATION2_2D" : "0.15625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_MAGNITUDE_2D" : "(8.25566537178801e-9*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1.284)**2*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8 + 2.29324038105222e-8*pi**2*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)**(1/2.)",

    "SOURCE_SATURATION1_2D" : "-5.97767711289092e-5*X[1]**2*(-2.5*X[1] + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1.284)*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*exp(-1.0*X[0])/(1.0*t + 1.) + 0.0625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 0.000151434486859903*pi*(1.64473684210526*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) - 1.31578947368421*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 0.000217056097832528*pi**2*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0]) - 0.000126195405716586*pi**2*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2",

    "DARCY_VELOCITY2_MAGNITUDE_2D" : "(2.45657642719267e-12*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)**2*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2 + 6.82382340886853e-12*pi**2*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)**(1/2.)",

    "SOURCE_SATURATION2_2D" : "5.15574650986842e-7*X[1]**2*(-2.5*X[1] + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*exp(-1.0*X[0])/(1.0*t + 1.) + 5.15574650986842e-7*X[1]**2*(-2.5*X[1] + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2 - 1000.0)*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.0625*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 2.61224489833333e-6*pi*(-0.822368421052632*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) + 0.657894736842105*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 2.61224489833333e-6*pi*(0.822368421052632*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) - 0.657894736842105*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 3.74421768761111e-6*pi**2*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0]) - 2.17687074861111e-6*pi**2*(0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.164473684210526*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2",

    "GRAVITY_DIRECTION_3D" : "1 0. 0. ",

    "PRESSURE_3D" : "(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])",

    "SATURATION1_3D" : "-0.54931640625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.",

    "SATURATION2_3D" : "0.54931640625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_MAGNITUDE_3D" : "(8.25566537178801e-9*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1.284)**2*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8 + 5.15979085736751e-8*pi**2*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*X[1])**4*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])**2*cos(1.25*pi*X[2])**2 + 2.29324038105222e-8*pi**2*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**8*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**4*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)**(1/2.)",

    "SOURCE_SATURATION1_3D" : "-0.000210152711000071*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1.284)*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*exp(-1.0*X[0])/(1.0*t + 1.) + 0.2197265625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 0.000227151730289855*pi*(8.67341694078947*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 4.62582236842105*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2]) - 0.000151434486859903*pi*(5.78227796052632*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 4.62582236842105*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**3*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 0.000500995760694847*pi**2*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0]) - 0.000283939662862319*pi**2*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])**2 - 0.000126195405716586*pi**2*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**4*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2",

    "DARCY_VELOCITY2_MAGNITUDE_3D" : "(2.45657642719267e-12*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)**2*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2 + 1.53536026699542e-11*pi**2*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*X[1])**4*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])**2*cos(1.25*pi*X[2])**2 + 6.82382340886853e-12*pi**2*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**4*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)**2*(25000.0*cos(1.0*pi*t) + 75000.0)**2*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**4*cos(1.0*pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)**(1/2.)",

    "SOURCE_SATURATION2_3D" : "1.81256713237562e-6*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*exp(-1.0*X[0])/(1.0*t + 1.) + 1.81256713237562e-6*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*(-1.0*pi*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.0*pi*X[0])*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2 - 1000.0)*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.2197265625*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 3.9183673475e-6*pi*(-4.33670847039474*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 2.31291118421053*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2]) + 3.9183673475e-6*pi*(4.33670847039474*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 2.31291118421053*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])*cos(1.0*pi*X[0])*cos(1.25*pi*X[2]) - 2.61224489833333e-6*pi*(-2.89113898026316*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 2.31291118421053*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 2.61224489833333e-6*pi*(2.89113898026316*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 2.31291118421053*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1]) + 8.64217687198611e-6*pi**2*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0]) - 4.897959184375e-6*pi**2*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(0.833333333333333*pi*X[1])**2*cos(1.0*pi*X[0])*cos(1.25*pi*X[2])**2 - 2.17687074861111e-6*pi**2*(0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.11022302462516e-16)**2*(-(-0.578227796052632*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0)**2 + 1.)*(25000.0*cos(1.0*pi*t) + 75000.0)*sin(1.25*pi*X[2])**2*cos(1.0*pi*X[0])*cos(0.833333333333333*pi*X[1])**2",

    }

