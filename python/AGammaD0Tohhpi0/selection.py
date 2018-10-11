'''Selections in TTree format.'''

from AnalysisUtils.selection import AND, OR

MC_sel_Dst_R = 'abs(lab0_TRUEID)==413 && abs(lab1_TRUEID)==421 && abs(lab5_TRUEID)==111 && abs(lab6_TRUEID)==22 && abs(lab7_TRUEID)==22 && abs(lab8_TRUEID)==211'
MC_sel_pipi_R = AND(MC_sel_Dst_R, 'abs(lab3_TRUEID)==211 && abs(lab4_TRUEID)==211 && lab0_MCMatch_pipi')
MC_sel_KK_R = AND(MC_sel_Dst_R, 'abs(lab3_TRUEID)==321 && abs(lab4_TRUEID)==321 && lab0_MCMatch_KK')
MC_sel_Kpi_R = AND(MC_sel_Dst_R, '((abs(lab3_TRUEID)==321 && abs(lab4_TRUEID)==211) || (abs(lab3_TRUEID)==211 && abs(lab4_TRUEID)==321)) && lab0_MCMatch_pipi')

masswindow_R = (1825, 1905)
masswindow_R_sel = '{0} < D0_mass && D0_mass < {1}'.format(*masswindow_R)

bdtcut = -0.1
bdtsel = 'BDT >= ' + str(bdtcut)

selection_R = AND(masswindow_R_sel, bdtsel)
