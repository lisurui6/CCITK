from pathlib import Path
from argparse import ArgumentParser
from .short_axis import eval_ventricular_volume, eval_wall_thickness, eval_strain_sax
from .long_axis import eval_atrial_volume, eval_strain_lax
from .aortic import eval_aortic_area


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--sa", action="store_true")
    parser.add_argument("--la", action="store_true")
    parser.add_argument("--ao", action="store_true")
    parser.add_argument("--data-dir", type=str, required=True)
    parser.add_argument("--output-csv", type=str, required=True)
    parser.add_argument("--pressure-csv", type=str, default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    data_dir = Path(args.data_dir).absolute()
    output_csv = Path(args.output_csv).absolute()
    par_dir = Path(__file__).parent.joinpath("par").absolute()
    if args.sa:
        eval_ventricular_volume(data_dir=str(data_dir), output_csv=str(output_csv))
        eval_wall_thickness(data_dir=str(data_dir), output_csv=str(output_csv))
        eval_strain_sax(data_dir=str(data_dir), output_csv=str(output_csv), par_dir=str(par_dir))

    if args.la:
        eval_atrial_volume(data_dir=str(data_dir), output_csv=str(output_csv))
        eval_strain_lax(data_dir=str(data_dir), output_csv=str(output_csv), par_dir=str(par_dir))

    if args.ao:
        assert args.pressure_csv is not None
        pressure_csv = Path(args.pressure_csv).absolute()
        eval_aortic_area(data_dir=str(data_dir), pressure_csv=str(pressure_csv), output_csv=str(output_csv))


if __name__ == '__main__':
    main()