import { Input, Outcome, Round, Shape } from "./model";

export const solveA = (content: Input) => {
  return content.map(playRound).reduce((p, v) => p + v, 0);
};

export const solveB = (content: Input) => {
  return content
    .map((r) => {
      return {
        opponent: r.opponent,
        mine: determineMine(r.opponent, r.mine as unknown as Outcome),
      };
    })
    .map(playRound)
    .reduce((p, v) => p + v, 0);
};

const BEATS = new Map<Shape, Shape>([
  [Shape.Rock, Shape.Scissors],
  [Shape.Paper, Shape.Rock],
  [Shape.Scissors, Shape.Paper],
]);
const SHAPE_SCORE = new Map<Shape, number>([
  [Shape.Rock, 1],
  [Shape.Paper, 2],
  [Shape.Scissors, 3],
]);
const OUTCOME_SCORE = new Map<Outcome, number>([
  [Outcome.Win, 6],
  [Outcome.Draw, 3],
  [Outcome.Loose, 0],
]);

const determineMine = (opponent: Shape, outcome: Outcome): Shape => {
  if (outcome == Outcome.Draw) {
    return opponent;
  }

  if (outcome == Outcome.Loose) {
    return BEATS.get(opponent)!;
  }

  for (const [a, b] of BEATS.entries()) {
    if (b == opponent) {
      return a;
    }
  }

  return undefined!;
};

const playRound = (round: Round): number => {
  const outcome = getOutcome(round);
  return SHAPE_SCORE.get(round.mine)! + OUTCOME_SCORE.get(outcome)!;
};

const getOutcome = (round: Round): Outcome => {
  if (round.mine == round.opponent) {
    return Outcome.Draw;
  }

  return BEATS.get(round.mine) == round.opponent ? Outcome.Win : Outcome.Loose;
};
