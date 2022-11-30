# Documentation about figures
 
First we had done a TSV file that's representing metadata about our 20 subjects.
```TSV
Sample-id	forward-absolute-filepath	reverse-absolute-filepath	Library Name	subject	body-site
Cresol-exposed-flora_recipient_Mouse_84pCre522	/Data/run_qiime/SRR14318758_1.fastq	/Data/run_qiime/SRR14318758_2.fastq	FMT2X84pCre522	FMT_GROUP1	FMT_GROUP
Cresol-exposed-flora_recipient_Mouse_83pCre499	/Data/run_qiime/SRR14318757_1.fastq	/Data/run_qiime/SRR14318757_2.fastq	FMT2X83pCre499	FMT_GROUP1	FMT_GROUP
Cresol-exposed-flora_recipient_Mouse_82pCre407	/Data/run_qiime/SRR14318756_1.fastq	/Data/run_qiime/SRR14318756_2.fastq	FMT2X82pCre407	FMT_GROUP1	FMT_GROUP
Cresol-exposed-flora_recipient_Mouse_81pCre13	/Data/run_qiime/SRR14318755_1.fastq	/Data/run_qiime/SRR14318755_2.fastq	FMT2X81pCre13	FMT_GROUP1	FMT_GROUP
Cresol-exposed-flora_recipient_Mouse_80pCre26	/Data/run_qiime/SRR14318754_1.fastq	/Data/run_qiime/SRR14318754_2.fastq	FMT2X80pCre26	FMT_GROUP1	FMT_GROUP
1stset_control_Mouse_1	/Data/run_qiime/SRR14318728_1.fastq	/Data/run_qiime/SRR14318728_2.fastq	CC_WC1	CC_WC	Control_water
1stset_control_Mouse_4	/Data/run_qiime/SRR14318727_1.fastq	/Data/run_qiime/SRR14318727_2.fastq	CC_WC4	CC_WC	Control_water
1stset_control_Mouse_3	/Data/run_qiime/SRR14318726_1.fastq	/Data/run_qiime/SRR14318726_2.fastq	CC_WC3	CC_WC	Control_water
1stset_control_Mouse_2	/Data/run_qiime/SRR14318725_1.fastq	/Data/run_qiime/SRR14318725_2.fastq	CC_WC2	CC_WC	Control_water
1stset_control_Mouse_15	/Data/run_qiime/SRR14318724_1.fastq	/Data/run_qiime/SRR14318724_2.fastq	CC_WC15	CC_WC	Control_water
Control_flora-recipient_Mouse_70W867	/Data/run_qiime/SRR14318801_1.fastq	/Data/run_qiime/SRR14318801_2.fastq	FMT2X70W867	FMT_GROUP2	FMT_Cresol
Control_flora-recipient_Mouse_69W546	/Data/run_qiime/SRR14318800_1.fastq	/Data/run_qiime/SRR14318800_2.fastq	FMT2X69W546	FMT_GROUP2	FMT_Cresol
Control_flora-recipient_Mouse_68W526	/Data/run_qiime/SRR14318799_1.fastq	/Data/run_qiime/SRR14318799_2.fastq	FMT2X68W526	FMT_GROUP2	FMT_Cresol
Control_flora-recipient_Mouse_67W800	/Data/run_qiime/SRR14318798_1.fastq	/Data/run_qiime/SRR14318798_2.fastq	FMT2X67W800	FMT_GROUP2	FMT_Cresol
Control_flora-recipient_Mouse_66w373	/Data/run_qiime/SRR14318797_1.fastq	/Data/run_qiime/SRR14318797_2.fastq	FMT2X66w373	FMT_GROUP2	FMT_Cresol
1stset_pCresol-exposed_Mouse_25	/Data/run_qiime/SRR14318771_1.fastq	/Data/run_qiime/SRR14318771_2.fastq	CC_PC25	CC_PC	PC_exposed
1stset_pCresol-exposed_Mouse_24	/Data/run_qiime/SRR14318770_1.fastq	/Data/run_qiime/SRR14318770_2.fastq	CC_PC24	CC_PC	PC_exposed
1stset_pCresol-exposed_Mouse_23	/Data/run_qiime/SRR14318769_1.fastq	/Data/run_qiime/SRR14318769_2.fastq	CC_PC23	CC_PC	PC_exposed
1stset_pCresol-exposed_Mouse_22	/Data/run_qiime/SRR14318768_1.fastq	/Data/run_qiime/SRR14318768_2.fastq	CC_PC22	CC_PC	PC_exposed
1stset_pCresol-exposed_Mouse_21	/Data/run_qiime/SRR14318767_1.fastq	/Data/run_qiime/SRR14318767_2.fastq	CC_PC21	CC_PC	PC_exposed
```
Then we have done a  sequence quality check using the Qimee 2 tool:

![SEQ_quality](/Doc/Sequence_Quality.png)


then we had check the beta diversity group significance still using qimee2 tool: 

![Beta_diversity_group_significance](/Doc/Beta_diversity_group_significance.png)


to finaly get do a PCA and a Taxinomic assignement :
![SEQ_quality](/Doc/PCA_with_Jaccard_q2-emperor-plot.png)



![SEQ_quality](/Doc/Taxonomic_assignment.png)
