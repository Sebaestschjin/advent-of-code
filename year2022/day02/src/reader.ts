import { lines } from "./lib";
import { Input, Round, Shape } from "./model";

const OPPONENT_SHAPE = new Map<string, Shape>([
  ["A", Shape.Rock],
  ["B", Shape.Paper],
  ["C", Shape.Scissors],
]);
const MINE_SHAPE = new Map<string, Shape>([
  ["X", Shape.Rock],
  ["Y", Shape.Paper],
  ["Z", Shape.Scissors],
]);

export const readData = (content: string): Input => {
  return lines(content).map(mapRound);
};

const mapRound = (row: string): Round => {
  const [opponent, mine] = row.split(" ");
  return {
    opponent: OPPONENT_SHAPE.get(opponent)!,
    mine: MINE_SHAPE.get(mine)!,
  };
};
