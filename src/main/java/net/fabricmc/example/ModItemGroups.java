package net.fabricmc.example;

import net.fabricmc.fabric.api.client.itemgroup.FabricItemGroupBuilder;
import net.minecraft.block.Blocks;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Identifier;

public class ModItemGroups {

    // Register Our Item Groups
    public static final ItemGroup TERRACOTTA_GROUP = FabricItemGroupBuilder.build(
            new Identifier("moreterracotta", "terracotta_group"),
            () -> new ItemStack(Blocks.TERRACOTTA));

    // Register Our Item Groups
    public static final ItemGroup CONCRETE_GROUP = FabricItemGroupBuilder.build(
            new Identifier("moreterracotta", "concrete_group"),
            () -> new ItemStack(Blocks.WHITE_CONCRETE));

}
