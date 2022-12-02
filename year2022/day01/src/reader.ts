import { Bagpack, Input } from "./model";

export const readData = (content: string): Input => {
  return parseBagpack(content).map(parseCalories);
};

const parseBagpack = (lines: string) => {
  return lines.split("\n\n");
};

const parseCalories = (bagpack: string): Bagpack => {
  return bagpack
    .split("\n")
    .filter((v) => v.trim().length > 0)
    .map((v) => Number.parseInt(v));
};
