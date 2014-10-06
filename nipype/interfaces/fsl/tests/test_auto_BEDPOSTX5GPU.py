# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import BEDPOSTX5GPU

def test_BEDPOSTX5GPU_inputs():
    input_map = dict(all_ard=dict(argstr='--allard',
    xor=('no_ard', 'all_ard'),
    ),
    args=dict(argstr='%s',
    ),
    burn_in=dict(argstr='--burnin=%d',
    ),
    burn_in_no_ard=dict(argstr='--burninnoard=%d',
    ),
    bvals=dict(argstr='--bvals=%s',
    mandatory=True,
    ),
    bvecs=dict(argstr='--bvecs=%s',
    mandatory=True,
    ),
    cnlinear=dict(argstr='--cnonlinear',
    xor=('no_spat', 'non_linear', 'cnlinear'),
    ),
    dwi=dict(argstr='--data=%s',
    mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    f0_ard=dict(argstr='--f0 --ardf0',
    xor=['f0_noard', 'f0_ard', 'all_ard'],
    ),
    f0_noard=dict(argstr='--f0',
    xor=['f0_noard', 'f0_ard'],
    ),
    force_dir=dict(argstr='--forcedir',
    usedefault=True,
    ),
    fudge=dict(argstr='--fudge=%d',
    ),
    gradnonlin=dict(argstr='-g',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    logdir=dict(argstr='--logdir=%s',
    usedefault=True,
    ),
    mask=dict(argstr='--mask=%s',
    mandatory=True,
    ),
    model=dict(argstr='--model=%d',
    ),
    n_fibres=dict(argstr='--nfibres=%d',
    ),
    n_jumps=dict(argstr='--njumps=%d',
    ),
    no_ard=dict(argstr='--noard',
    xor=('no_ard', 'all_ard'),
    ),
    no_spat=dict(argstr='--nospat',
    xor=('no_spat', 'non_linear', 'cnlinear'),
    ),
    non_linear=dict(argstr='--nonlinear',
    xor=('no_spat', 'non_linear', 'cnlinear'),
    ),
    out_dir=dict(argstr='%s',
    mandatory=True,
    position=1,
    usedefault=True,
    ),
    output_type=dict(),
    rician=dict(argstr='--rician',
    ),
    sample_every=dict(argstr='--sampleevery=%d',
    ),
    seed=dict(argstr='--seed=%d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    update_proposal_every=dict(argstr='--updateproposalevery=%d',
    ),
    )
    inputs = BEDPOSTX5GPU.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BEDPOSTX5GPU_outputs():
    output_map = dict(d_stdsamples=dict(),
    dsamples=dict(),
    dyads=dict(),
    dyads_disp=dict(),
    fsamples=dict(),
    mean_S0samples=dict(),
    mean_d_stdsamples=dict(),
    mean_dsamples=dict(),
    mean_fsamples=dict(),
    mean_phsamples=dict(),
    mean_tausamples=dict(),
    mean_thsamples=dict(),
    merged_fsamples=dict(),
    merged_phsamples=dict(),
    merged_thsamples=dict(),
    phsamples=dict(),
    thsamples=dict(),
    )
    outputs = BEDPOSTX5GPU.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

