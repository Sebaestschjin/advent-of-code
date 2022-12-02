export type Input = Round[];

export interface Round {
  opponent: Shape;
  mine: Shape;
}

export const enum Outcome {
  Loose,
  Draw,
  Win,
}

export const enum Shape {
  Rock,
  Paper,
  Scissors,
}
