## Character Error Rate helper function.

def compute_CER(predicted_text = "", ground_truth = ""):
    """
    Function to compute the Character Error Rate (CER) between the predicted text and the ground truth.
    
    Arguments:
    predicted_text : str : The predicted text.
    ground_truth : str : The ground truth text.
    """
    # Remove all spaces from the predicted text and the ground truth.
    predicted_text = predicted_text.replace(" ", "").lower()
    ground_truth = ground_truth.replace(" ", "").lower()
    
    # Get the length of the predicted text and the ground truth.
    len_predicted_text = len(predicted_text)
    len_ground_truth = len(ground_truth)
    
    # If the predicted text is empty, then the CER is the length of the ground truth.
    if len_predicted_text == 0:
        return len_ground_truth
    
    # If the ground truth is empty, then the CER is the length of the predicted text.
    if len_ground_truth == 0:
        return len_predicted_text
    
    # Create a matrix of size (len_predicted_text + 1) x (len_ground_truth + 1) to store the CER values.
    cer_matrix = [[0 for _ in range(len_ground_truth + 1)] for _ in range(len_predicted_text + 1)]
    
    # Initialize the first row and the first column of the matrix.
    for i in range(len_predicted_text + 1):
        cer_matrix[i][0] = i
    for j in range(len_ground_truth + 1):
        cer_matrix[0][j] = j
    
    # Compute the CER values.
    for i in range(1, len_predicted_text + 1):
        for j in range(1, len_ground_truth + 1):
            if predicted_text[i - 1] == ground_truth[j - 1]:
                cer_matrix[i][j] = cer_matrix[i - 1][j - 1]
            else:
                cer_matrix[i][j] = min(cer_matrix[i - 1][j - 1], cer_matrix[i][j - 1], cer_matrix[i - 1][j]) + 1
    
    # Return the CER value.
    sdi = cer_matrix[len_predicted_text][len_ground_truth]
    
    cer = (sdi / len(ground_truth)) * 100
    return cer


predicted_text = "LOrem ipSum dOLOr Sit ameto EX quiSquam quiSquam id eXpLiCabO iLLum hiC amet eVenieto HiC dOLOreS fugiat ut neSCiunt neSCiunt VeL pOSSimuS quiSquam eOS quam tempOribuS et repudiandae Veniam nOnWniam nemOo Qui Veniam dOLOrSed quia enimaut dOLOremque OffiCia qui aSpernatur impedit a enim tOtam At OptiO atqueo Id COnSequatur repudiandae hiCVOLuptate eLigendi et Cupiditate natuS eaOptiOdOLOremSed eXerCitatiOnemVeLito In eLigendi LabOrum et WLuptaS pariatur et quaSi rerum Sit quidem rerumo ESt magni animi eum inCidunt neque aut Sint VeritatiS eum mOdi WLuptaSl HiC diCta pariatur aut internOS LabOrum Sed OmniS repeLLat aut LabOrum nemO qui nObiStOtam nOn impedit ratiOne eSt QuiS tOtamo In quia VOLuptaS ea neque eLigendi et eXCepturi aSperiOreSo"
ground_truth = "Lorem ipsum dolor sit amet. Ex quisquam quisquam id explicabo illum hic amet eveniet. Hic dolores fugiat ut nesciunt nesciunt vel possimus quisquam eos quam temporibus et repudiandae veniam non veniam nemo. Qui veniam dolor sed quia enim aut doloremque officia qui aspernatur impedit a enim totam At optio atque. Id consequatur repudiandae hic voluptate eligendi et cupiditate natus ea optio dolorem sed exercitationem velit. In eligendi laborum et voluptas pariatur et quasi rerum sit quidem rerum. Est magni animi eum incidunt neque aut sint veritatis eum modi voluptas! Hic dicta pariatur aut internos laborum sed omnis repellat aut laborum nemo qui nobis totam non impedit ratione est Quis totam. In quia voluptas ea neque eligendi et excepturi asperiores."

print(compute_CER(predicted_text, ground_truth))