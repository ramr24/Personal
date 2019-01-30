import pandas as pd

post_patch_column = "Post patch?"
post_patch_pipette_column = "Post patch pipette R"

def nucleated(x):
    nuc_high_seal = x[(x[post_patch_column] == 'Nucleated') | 
                      (((x[post_patch_column] == 'nucleus_visible') | 
                      (x[post_patch_column] == 'nucleus_present')) & 
                      (x[post_patch_pipette_column] >= 50))]
    return nuc_high_seal

def partial_nucleated(y):
    nuc_low_seal = y[(y[post_patch_column] == 'Partial-Nucleus') | 
                     (((y[post_patch_column] == 'nucleus_present') | 
                     (y[post_patch_column] == 'nucleus_visible')) & 
                     (y[post_patch_pipette_column] < 50))]
    return nuc_low_seal

def outside_out(z):
    no_high_seal = z[(z[post_patch_column] == 'Outside-Out') | 
                     (((z[post_patch_column] == 'nucleus_absent') | 
                     (z[post_patch_column] == 'no_nucleus_visible')) & 
                     (z[post_patch_pipette_column] >= 50))]
    return no_high_seal

def no_seal(w): 
    no_low_seal = w[(w[post_patch_column] == 'No-Seal') | 
                    (((w[post_patch_column] == 'nucleus_absent') | 
                    (w[post_patch_column] == 'no_nucleus_visible')) & 
                    (w[post_patch_pipette_column] < 50))]
    return no_low_seal
    
def entire_cell(v):
    entire = v[(v[post_patch_column] == 'Entire-Cell') | 
               (v[post_patch_column] == 'entire_cell')]
    return entire

#variable['post_patch'] = 'Term'
#Term is an output displayed in the Post_Patch column

def reclassify(df):
    nu = nucleated(df)
    nu.loc[:,'post_patch'] = 'Nuc-high seal' 
    oo = outside_out(df)
    oo.loc[:,'post_patch'] = 'No-high seal'
    pn = partial_nucleated(df)
    pn.loc[:,'post_patch'] = 'Nuc-low seal'
    ns = no_seal(df)
    ns.loc[:,'post_patch'] = 'No-low seal'
    ec = entire_cell(df)
    ec.loc[:,'post_patch'] = 'Entire cell'
    return  nu, oo, pn, ns, ec

def concat_df(a, b, c, d, e):
    frames = (a, b, c, d, e)
    df = pd.concat(frames)
    return df

def postpatch_reclass(df):
    return concat_df(*reclassify(df))

#df = postpatch_reclass(df)