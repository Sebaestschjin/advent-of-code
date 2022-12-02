import { sum } from "./lib";
import { Calory, Input } from "./model";

export const solveA = (content: Input) => {
  return createTopList(content).at(-1);
};

export const solveB = (content: Input) => {
  return createTopList(content)
    .slice(-3)
    .reduce((p, v) => p + v, 0);
};

const createTopList = (content: Input): Calory[] => {
  return content.map(sum).sort((a, b) => a - b);
};
