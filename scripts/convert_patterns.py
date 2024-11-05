
from pathlib import Path
import typer



def main(
    infile: Path = typer.Argument(..., help="Input file to convert"),
    outfile: Path = typer.Argument(..., help="Ouput file to write"),
) -> None:
    infile_format = infile.suffix[1:]
    outfile_format = outfile.suffix[1:]

    pass

if __name__ == "__main__":
    typer.run(main)
